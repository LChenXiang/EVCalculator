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


if __name__ == '__main__':
    # load these test suits
    solar_calc_suit = unittest.TestLoader().loadTestsFromTestCase(TestSolarEnergyPastCalculator)
    # run the test suits
    unittest.TextTestRunner(verbosity=2).run(solar_calc_suit)
