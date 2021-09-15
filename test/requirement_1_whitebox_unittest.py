from app.calculator import *
import unittest
from datetime import time, date


class WhiteBoxCostCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.postcode = "4000"

    def test_whitebox_totalcost_tc1(self):
        """
        Path coverage test case 1 for total_cost_calculation.
        """
        config = 1
        start_time = time(8)
        start_date = date(2021, 8, 24)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 0.55
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

    def test_whitebox_totalcost_tc2(self):
        """
        Path coverage test case 2 for total_cost_calculation.
        """
        config = 1
        start_time = time(0)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 0.25
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

    def test_whitebox_totalcost_tc3(self):
        """
        Path coverage test case 3 for total_cost_calculation.
        """
        config = 3
        start_time = time(8)
        start_date = date(2021, 8, 21)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 1
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

    def test_whitebox_totalcost_tc4(self):
        """
        Path coverage test case 4 for total_cost_calculation.
        """
        config = 4
        start_time = time(0)
        start_date = date(2021, 8, 24)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_cost = 0.69
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

    def test_whitebox_cost_calculation_tc1(self):
        """
        Path coverage test
        :return:
        """
        initial_state = 20
        final_state = 40
        capacity = 50
        base_price = 5
        is_holiday = True
        is_peak = True
        expected_cost = 0.55

        final_cost = self.calculator.cost_calculation(initial_state=initial_state, final_state=final_state,
                                                      capacity=capacity, is_holiday=is_holiday, is_peak=is_peak,
                                                      base_price=base_price)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_cost_calculation_tc2(self):
        initial_state = 20
        final_state = 40
        capacity = 50
        base_price = 12.5
        is_holiday = True
        is_peak = False
        expected_cost = 0.69

        final_cost = self.calculator.cost_calculation(initial_state=initial_state, final_state=final_state,
                                                      capacity=capacity, is_holiday=is_holiday, is_peak=is_peak,
                                                      base_price=base_price)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_cost_calculation_tc3(self):
        initial_state = 20
        final_state = 40
        capacity = 50
        base_price = 10
        is_holiday = False
        is_peak = True
        expected_cost = 1

        final_cost = self.calculator.cost_calculation(initial_state=initial_state, final_state=final_state,
                                                      capacity=capacity, is_holiday=is_holiday, is_peak=is_peak,
                                                      base_price=base_price)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_cost_calculation_tc4(self):
        initial_state = 20
        final_state = 40
        capacity = 50
        base_price = 5
        is_holiday = False
        is_peak = False
        expected_cost = 0.25

        final_cost = self.calculator.cost_calculation(initial_state=initial_state, final_state=final_state,
                                                      capacity=capacity, is_holiday=is_holiday, is_peak=is_peak,
                                                      base_price=base_price)
        self.assertAlmostEqual(final_cost, expected_cost, delta=0.01, msg=("Expected %s, got %s instead"
                                                                           % (expected_cost, final_cost)))

    def test_whitebox_time_calculation_tc1(self):
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        expected_time = 5
        power = 2
        charge_time = self.calculator.time_calculation(initial_state=initial_charge, final_state=final_charge,
                                                       capacity=battery_capacity, power=power)
        self.assertEqual(expected_time, charge_time, msg=("Expected %s, got %s instead" %
                                                          (expected_time, charge_time)))

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
