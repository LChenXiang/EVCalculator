from app.calculator import *
import unittest
from datetime import date

class TestStateHolidays(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_state_holidays_1(self):
        state_str = "WA"
        easter_sat = date(2021, 4, 3) # Western Australia doesn't have any holidays here...
        self.assertFalse(self.calculator.is_holiday(easter_sat, state_str))

    def test_state_holidays2(self):
        state_str = "ACT"
        easter_sat = date(2021, 4, 3)
        self.assertTrue(self.calculator.is_holiday(easter_sat, state_str))



if __name__ == "__main__":
    # create the test suit from the cases above.
    suit = unittest.TestLoader().loadTestsFromTestCase(TestStateHolidays)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)