from app.calculator import *
import unittest
from datetime import date, time


class TestSolarEnergyPastCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.postcode = "4000"

    def solar_energy_past_testcase1(self):
        """
        Path coverage for test case 1 of calculate_solar_energy_past_to_currentday_minus_two
        """
        pass

    def solar_energy_past_testcase2(self):
        """
        Path coverage for test case 2 of calculate_solar_energy_past_to_currentday_minus_two
        """
        pass

    def solar_energy_past_testcase3(self):
        """
        Path coverage for test case 3 of calculate_solar_energy_past_to_currentday_minus_two
        """
        pass

    def solar_energy_past_testcase4(self):
        """
        Path coverage for test case 4 of calculate_solar_energy_past_to_currentday_minus_two
        """
        pass


if __name__ == '__main__':
    # load this test suit
    suit = unittest.TestLoader().loadTestsFromTestCase(TestSolarEnergyPastCalculator)
    # run this test suit
    unittest.TextTestRunner(verbosity=2).run(suit)
