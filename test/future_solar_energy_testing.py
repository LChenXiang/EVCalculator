from app.calculator import *
import unittest


class TestFutureSolar(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_1(self):
        """
            solar_testing
            condition: This path is when the start time and end time is not within daylight length, thus it will return directly as there will be no solar energy generated
        """
        start_time = datetime(2021, 2, 22, 1, 30)
        end_time = datetime(2021, 2, 22, 2, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0
        self.assertAlmostEqual(solar_energy_generated, expected_result, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_2(self):
        """
            solar_testing
            condition: This path is when the start time hour is the same as sunrise hour but the start time minute is smaller than the sunrise minute,
            it will update the value of start time. Then, path 8-9-10 will not be possible as path 8-9-10 indicates the start time to end time is a whole hour, 
            which won’t happen as if the start time minute is smaller than sunrise minute it won’t be a whole hour.
        """
        start_time = datetime(2021, 2, 22, 5, 00)
        end_time = datetime(2021, 2, 22, 6, 00)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0.99
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_3(self):
        """
            solar_testing
            condition: This path is when the end time hour is the same as sunset hour but the end time minute is larger than the sunset minute, 
            it will update the value of end time. Then, path 8-9-10 will not be possible as path 8-9-10 indicates the start time to end time is a whole hour, 
            which won’t happen as if the end time minute is smaller than sunset minute it won’t be a whole hour.
        """
        start_time = datetime(2021, 2, 22, 19, 00)
        end_time = datetime(2021, 2, 22, 20, 00)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0.34
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_4(self):
        """
            solar_testing
            condition: This path is when the start time and end time has a whole hour gap which is 60 minutes. The value of du will be updated to 1.
        """
        start_time = datetime(2021, 2, 22, 17, 00)
        end_time = datetime(2021, 2, 22, 18, 00)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 3.25
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))
    def test_5(self):
        """
            cost_calculation
            condition: cost calculation
        """
        config = 3
        start_time = time(17,30)
        start_date = date(2022, 2, 22)
        battery_capacity = 50
        initial_charge = 20
        final_charge = 40
        power = self.calculator.get_configuration(config)[0]
        base_cost = self.calculator.get_configuration(config)[1]
        end_time = datetime(2022,2,22,18,15)   
        final_cost = self.calculator.total_cost_calculation(start_date=start_date, start_time=start_time,
                                                                start_state=initial_charge, end_time=end_time,
                                                                base_price=base_cost, power=power,
                                                                capacity=battery_capacity, postcode="7250",solar_energy=True)
        expected_output = 0.22
        self.assertAlmostEqual(final_cost, expected_output, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_output, final_cost)))

    # you may create test suite if needed
    # Test case needed for form
if __name__ == "__main__":
    unittest.main()
