import sys

sys.path.insert(1, "..")

from app.calculator import *
import unittest
from datetime import time, date


class TestSunHours(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_sunHours_1(self):
        input_date = date(2021, 8, 1)
        postcode = "3800"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 10.2
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))
    def test_sunHours_2(self):
        input_date = date(2021, 8, 1)
        postcode = "4000"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 10.85
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))
    def test_sunHours_3(self):
        input_date = date(2021, 8, 20)
        postcode = "3200"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 0 #10.8334
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))


if __name__ == "__main__":
    # create the test suit from the cases above.
    sunHoursSuit = unittest.TestLoader().loadTestsFromTestCase(TestSunHours)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(sunHoursSuit)
