from app.calculator import *
import unittest
from datetime import datetime


class TestSolarEnergyPastCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.postcode = "4000"

    def test_solar_energy_past_testcase1(self):
        """
        Path coverage for test case 1 of calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 7, 1, 12, 30)
        end = datetime(2008, 7, 1, 13)
        expected = 1.82
        actual = self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)
        self.assertAlmostEqual(actual, expected, delta=0.01, msg=("Expected %s, Got %s instead") % (expected, actual))

    def test_solar_energy_past_testcase2(self):
        """
        Path coverage for test case 2 of calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 6, 30)
        end = datetime(2008, 6, 30, 1)
        expected = 0
        actual = self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))

    def test_solar_energy_past_test_diff_date(self):
        """
        Path coverage for datetime validation test for calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 7, 2)
        end = datetime(2008, 7, 1)
        with self.assertRaises(ValueError):
            self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)

    def test_solar_energy_past_test_invalid_hours_interval(self):
        """
        Path coverage for datetime validation test for calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 7, 1, 12, 1)
        end = datetime(2008, 7, 1, 13, 5)
        with self.assertRaises(ValueError):
            self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)


class TestSolarEnergyDuration(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.postcode = "4000"
        self.date = date(2021, 9, 10)

    def test_solar_energy_duration_error(self):
        """
        Checks if ValueError is raised in appropriate cases (test case 1)
        """
        start = time(13)
        end = time(12)
        with self.assertRaises(ValueError):
            self.calculator.get_solar_energy_duration(start, end, self.date, self.postcode)

    def test_solar_energy_duration_start_during_sunset(self):
        """
        Ensures that function returns 0 if start time is during sunset (test case 2)
        """
        start = time(22)
        end = time(23)
        expected = 0
        actual = self.calculator.get_solar_energy_duration(start, end, self.date, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))

    def test_solar_energy_duration_normal(self):
        """
        Test case for normal inputs (test case 3)
        """
        start = time(12, 30)
        end = time(13)
        expected = 0.5
        actual = self.calculator.get_solar_energy_duration(start, end, self.date, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))


if __name__ == '__main__':
    # load these test suits
    solar_calc_suit = unittest.TestLoader().loadTestsFromTestCase(TestSolarEnergyPastCalculator)
    solar_dur_suit = unittest.TestLoader().loadTestsFromTestCase(TestSolarEnergyDuration)

    # run the test suits
    unittest.TextTestRunner(verbosity=2).run(solar_calc_suit)
    unittest.TextTestRunner(verbosity=2).run(solar_dur_suit)
