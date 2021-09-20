from app.calculator import *
import unittest

"""

1-2-4-8-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
1-2-4-9-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
1-2-5-10-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
1-2-5-11-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
1-2-6-18-19-20-22-25-19-(20-24-25-19)x(n)-20-23-25-26-19-27-Return 
1-3-7-12-14-15-16-17-18-19-20-21-25-26-19-27-Return
1-3-7-12-15-16-17-18-19-20-22-25-19-20-23-25-26-19-27-Return
1-3-7-12-14-15-17-18-19-20-22-25-19-20-23-25-26-19-27-Return
1-3-7-12-15-17-18-19-20-21-25-26-19-27-Return
1-3-7-13-Return

"""

class TestFutureSolar(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_1(self):
        """
            Path coverage:
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
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass

    def test_10(self):
        pass

    # you may create test suite if needed
    # Test case needed for form
if __name__ == "__main__":
    unittest.main()
