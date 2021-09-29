from app.calculator import *
import unittest
from datetime import date, time


class TestSolarEnergyDuration(unittest.TestCase):
    # t1- error , t2-start>sunset, t3-normal
    def setUp(self) -> None:
        self.calculator = Calculator()

    def solar_energy_duration_testerror(self):
        """
        Checks if ValueError is raised in appropriate cases
        """
        pass

    def solar_energy_duration_test_start_during_sunset(self):
        """
        Ensures that function returns 0 if start time is during sunset
        """
        pass

    def solar_energy_duration_test_normal(self):
        """
        Test case for normal inputs
        """
        pass

    
if __name__ == '__main__':
    # load this test suit
    suit = unittest.TestLoader().loadTestsFromTestCase(TestSolarEnergyDuration)
    # run this test suit
    unittest.TextTestRunner(verbosity=2).run(suit)
