from app.calculator import *
import unittest
import datetime


class TestSolarEnergyPastCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.postcode = "4000"

    def solar_energy_past_testcase1(self):
        """
        Path coverage for test case 1 of calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008,7,1,12)
        end = datetime(2008,7,1,13)
        expected = 0
        actual = self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))

    def solar_energy_past_testcase2(self):
        """
        Path coverage for test case 2 of calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 6, 30)
        end = datetime(2008, 6, 30, 1)
        expected = 0
        actual = self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)
        self.assertEqual(actual, expected, msg=("Expected %s, Got %s instead") % (expected, actual))

    def solar_energy_past_test_diff_date(self):
        """
        Path coverage for test case 3 of calculate_solar_energy_past_to_currentday_minus_two
        """
        start = datetime(2008, 7, 1)
        end = datetime(2008, 7, 2)
        with self.assertRaises(ValueError):
            self.calculator.calculate_solar_energy_past_to_currentday_minus_two(start, end, self.postcode)


if __name__ == '__main__':
    # load these test suits
    solar_calc_suit = unittest.TestLoader().loadTestsFromTestCase(TestSolarEnergyPastCalculator)
    # run the test suits
    unittest.TextTestRunner(verbosity=2).run(solar_calc_suit)
