from app.calculator import *
import unittest


class TestFutureSolar(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_1(self):
        """
            condition: start_time and end_time has 1 or more day gap, current_date is start_date, target in between sunrise_delta and sunset_delta, first iteration is start_time, n iteration is for full hour, last iteration is sunset_time
            1-2-4-8-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
        """
        start_time = datetime(2022, 2, 22, 17, 30)
        end_time = datetime(2022, 2, 22, 18, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_2(self):
        """
            condition: start_time and end_time has 1 or more day gap, current_date is start_date, target is larger than sunrise_delta, there will be no iteration as start_time is not within daylight at the start_date
            Path coverage:
            1-2-4-9-18-19-27-Return
        """
        start_time = datetime(2022, 2, 22, 17, 30)
        end_time = datetime(2022, 2, 22, 18, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_3(self):
        """
            condition: start_time and end_time has 1 or more day gap, current_date is start_date, target is smaller than sunrise_delta, first iteration is sunrise_time, n iteration is for full hour, last iteration is sunset_time
            Path coverage:
            1-2-4-28-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return
        """
        start_time = datetime(2022, 2, 22, 17, 30)
        end_time = datetime(2022, 2, 22, 18, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_4(self):
        """
            condition: start_time and end_time has 1 or more day gap, current_date is end_date, target in between sunrise_delta and sunset_delta, first iteration is sunrise_time, n iteration is for full hour, last iteration is end_time
            Path coverage:
            1-2-5-10-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
        """
        start_time = datetime(2022, 2, 22, 17, 30)
        end_time = datetime(2022, 2, 22, 18, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_5(self):
        """
            condition: start_time and end_time has 1 or more day gap, current_date is end_date, target is smaller than sunrise_time, there will be no iteration as end_time is not within daylight at the end_date
            Path coverage:
            1-2-5-11-18-19-27-Return
        """
        start_time = datetime(2022, 2, 22, 17, 30)
        end_time = datetime(2022, 2, 22, 18, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_6(self):
        """
            condition: start_time and end_time has 1 or more day gap, current_date is end_date, the end_time is larger than sunset_delta, first iteration is sunrise_time, n iteration is for full hour, last iteration is sunset_time
            Path coverage:
            1-2-5-29-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return
        """
        start_time = datetime(2022, 2, 22, 17, 30)
        end_time = datetime(2022, 2, 22, 18, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_7(self):
        """
            condition: start_time and end_time has 1 or more day gap, current_date is not start_date or end_date, first iteration is sunrise_time, n iteration is for full hour, last iteration is sunset_time
            Path coverage:
            1-2-6-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
        """
        start_time = datetime(2022, 2, 22, 17, 30)
        end_time = datetime(2022, 2, 22, 18, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_8(self):
        """
            condition: start_time was before sunrise, end_time was after sunset, first iteration is sunrise_time, n iteration is for full hour, last iteration is sunset_time
            Path coverage:
            1-3-7-12-14-15-16-17-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return
        """
        start_time = datetime(2022, 2, 22, 4, 30)
        end_time = datetime(2022, 2, 22, 20, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_9(self):
        """
            condition: start_time is in daylight range, end_time was after sunset, first iteration is start_time and sunset_time
            Path coverage:
            1-3-7-12-15-16-17-18-19-20-21-25-26-19-27-Return
        """
        start_time = datetime(2022, 2, 22, 19, 00)
        end_time = datetime(2022, 2, 22, 19, 30)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_10(self):
        """
            condition: start_time was before sunrise, end_time is in daylight range, first iteration is sunrise_time,n iteration is for full hour, last iteration is end_time
            Path coverage:
            1-3-7-12-14-15-17-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
        """
        start_time = datetime(2022, 2, 22, 5, 30)
        end_time = datetime(2022, 2, 22, 9, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 6.72
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_11(self):
        """
            condition: time input was in between sunrise and sunset, first iteration is start_time, second iteration is end_time
            Path coverage:
            1-3-7-12-15-17-18-19-20-22-25-19-20-23-25-26-19-27-Return
        """
        start_time = datetime(2022, 2, 22, 17, 30)
        end_time = datetime(2022, 2, 22, 18, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 2.9
        self.assertAlmostEqual(solar_energy_generated, expected_result, delta=0.01, msg=("Expected %s, got %s instead"
                                                                                         % (expected_result, solar_energy_generated)))

    def test_12(self):
        """
            Condition: time input was not daylight
            Path coverage:
            1-3-7-13-Return
        """
        start_time = datetime(2022, 2, 22, 20, 30)
        end_time = datetime(2022, 2, 22, 21, 15)
        postcode = "7250"
        solar_energy_generated = self.calculator.calculate_solar_energy_future(
            start_time, end_time, postcode)
        expected_result = 0
        self.assertAlmostEqual(solar_energy_generated, expected_result, msg=("Expected %s, got %s instead"
                                                                             % (expected_result, solar_energy_generated)))


    # you may create test suite if needed
    # Test case needed for form
if __name__ == "__main__":
    unittest.main()
