from app.calculator import *
import unittest
from datetime import time, date


class WhiteBoxCostCalculator(unittest.TestCase):
    """
    In the Cost calculator, we will use branch coverage here
    This is because there are only some simple conditions that controls the flow of the code.
    """

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.postcode = "4000"

    def test_white_box_branch_1(self):
        """
        We will test the branch of non-holiday weekend on both peak and non peak hours.
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 4.2
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode)

        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_white_box_branch_2(self):
        """
        We will test the branch of holidays/weekdays branch of peak and non-peak hours.
        """
        config = 3
        start_time = time(16, 50)
        start_date = date(2021, 8, 20)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 2.11
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode)

        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_white_box_invalid_end_date(self):
        """
        We will test what happens when the end date is earlier than the start date.
        In this case, there should be 0 charge at all, at the backend.
        Frontend wise, this should be caught by calculator_form.py
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 0
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        # end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        end_time = datetime(2020, 8, 21, 5, 30)
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                            start_state=initial_charge, end_time=end_time,
                                                            base_price=base_cost, power=power,
                                                            capacity=battery_capacity, postcode=self.postcode)

        self.assertEqual(final_cost, expected_cost, msg=("Expected %s, got %s instead" % (expected_cost, final_cost)))

    def test_whitebox_invalid_time(self):
        """
        We will test what happens if we supply invalid start date
        """
        config = 6
        start_time = time(5, 30)
        start_date = "2021-8-31"
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 0
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        # end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(TypeError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode)

    def test_whitebox_invalid_date(self):
        """
        We will test what happens if we supply invalid start_time type
        """
        config = 6
        start_time = "5:30"
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        expected_cost = 0
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        # end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        end_time = datetime(2020, 8, 21, 5, 30)
        with self.assertRaises(TypeError):
            final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode=self.postcode)

    def test_whitebox_invalid_type_isoc(self):
        """
        We will test what happens if we supply wrong isoc type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = "20"
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)
    def test_whitebox_invalid_type_battery(self):
        """
        We will test what happens if we supply wrong battery capacity type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = "50"
        initial_charge = 20
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)

    def test_whitebox_invalid_type_power(self):
        """
        We will test what happens if we supply wrong power type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        power = str(self.calculator.get_configuration(config)[0])
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)

    def test_whitebox_invalid_type_base_cost(self):
        """
        We will test what happens if we supply wrong base_cost type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = str(self.calculator.get_configuration(config)[1])
        charge_time = 4
        end_time = self.calculator.get_end_time(start_date, start_time, charge_time)
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)

    def test_whitebox_invalid_type_end_time(self):
        """
        We will test what happens if we supply wrong base_cost type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = "2021/8/21"
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=self.postcode)
    def test_whitebox_invalid_type_postcode(self):
        """
        We will test what happens if we supply wrong base_cost type
        """
        config = 6
        start_time = time(5, 30)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 80
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        charge_time = 4
        end_time = "2021/8/21"
        with self.assertRaises(TypeError):
            self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                   start_state=initial_charge, end_time=end_time,
                                                   base_price=base_cost, power=power, capacity=battery_capacity,
                                                   postcode=4000)



if __name__ == "__main__":
    # create the test suit from the cases above.
    suit = unittest.TestLoader().loadTestsFromTestCase(WhiteBoxCostCalculator)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)
