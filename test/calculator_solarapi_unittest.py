from app.calculator import *
import unittest
from datetime import time, date


class TestDaylightLength(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_DaylightLength_1(self):
        input_date = date(2021, 8, 1)
        postcode = "3800"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 10.2
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))

    def test_DaylightLength_2(self):
        input_date = date(2021, 8, 1)
        postcode = "4000"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 10.85
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))

    def test_DaylightLength_3(self):
        input_date = date(2021, 8, 20)
        postcode = "3200"
        res = self.calculator.get_day_light_length(input_date, postcode)
        expected_output = 10.8334
        self.assertAlmostEqual(res, expected_output, delta=0.01, msg=("Expected %s, got %s" %
                                                                      (expected_output, res)))

    def test_DaylightLength_error_invalid_postcode_1(self):
        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="0000", input_date=date(year=2021, month=8, day=20))

    def test_DaylightLength_error_invalid_postcode_2(self):
        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="00", input_date=date(year=2021, month=8, day=20))

    def test_DaylightLength_error_invalid_date(self):
        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="00", input_date=date(year=2000, month=8, day=20))


class TestSunHours(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_SunHours_1(self):
        input_date = date(2021, 8, 1)
        postcode = "3800"
        res = self.calculator.get_sun_hour(input_date, postcode)
        expected_output = 3.2
        self.assertEqual(res, expected_output, msg=("Expected %s, got %s" % (expected_output, res)))

    def test_SunHours_2(self):
        input_date = date(2021, 8, 2)
        postcode = "4000"
        res = self.calculator.get_sun_hour(input_date, postcode)
        expected_output = 3.5
        self.assertEqual(res, expected_output, msg=("Expected %s, got %s" % (expected_output, res)))

    def test_SunHours_3(self):
        input_date = date(2021, 8, 20)
        postcode = "3200"
        res = self.calculator.get_sun_hour(input_date, postcode)
        expected_output = 2.6
        self.assertEqual(res, expected_output, msg=("Expected %s, got %s" % (expected_output, res)))

    def test_SunHours_error_invalid_postcode_1(self):
        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="0000", input_date=date(year=2021, month=8, day=20))

    def test_SunHours_error_invalid_postcode_2(self):
        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="00", input_date=date(year=2021, month=8, day=20))

    def test_SunHours_error_invalid_date(self):
        with self.assertRaises(ValueError):
            self.calculator.get_sun_hour(postcode="00", input_date=date(year=2000, month=8, day=20))


class TestGetSunriseSunSet(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_SRSS_1(self):
        input_date = date(2021, 8, 1)
        postcode = "3800"
        res = self.calculator.get_sunrise_sunset(input_date, postcode)
        expected_sunrise = time(hour=7, minute=20, second=0)
        expected_sunset = time(hour=17, minute=32, second=0)
        expected_output = (expected_sunrise, expected_sunset)
        self.assertEqual(expected_sunrise, res[0], msg=("Expected %s, got %s" % (expected_sunrise, res[0])))
        self.assertEqual(expected_sunset, res[1], msg=("Expected %s, got %s" % (expected_sunset, res[1])))

    def test_SRSS_2(self):
        input_date = date(2021, 8, 2)
        postcode = "4000"
        res = self.calculator.get_sunrise_sunset(input_date, postcode)
        expected_sunrise = time(hour=6, minute=28, second=0)
        expected_sunset = time(hour=17, minute=20, second=0)
        expected_output = (expected_sunrise, expected_sunset)
        self.assertEqual(expected_sunrise, res[0], msg=("Expected %s, got %s" % (expected_sunrise, res[0])))
        self.assertEqual(expected_sunset, res[1], msg=("Expected %s, got %s" % (expected_sunset, res[1])))


class TestCloudCover(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_cloud_cover_1(self):
        input_date = date(2021, 8, 2)
        postcode = "4000"
        excepted_list = [12, 12, 12, 13, 13, 12, 12, 13,
                         13, 14, 13, 12, 11, 20, 29, 37,
                         48, 59, 69, 75, 81, 87, 79, 72]
        res = self.calculator.get_cloud_cover(input_date, postcode)
        self.assertEqual(res, excepted_list, msg=("Excepted %s, got %s" % (excepted_list, res)))

    def test_cloud_cover_2(self):
        input_date = date(2021, 8, 1)
        postcode = "3800"
        excepted_list = [100, 94, 87, 81, 79, 78, 76, 78,
                         80, 82, 67, 51, 35, 30, 24, 18,
                         18, 19, 19, 16, 13, 10, 8, 7]
        res = self.calculator.get_cloud_cover(input_date, postcode)
        self.assertEqual(res, excepted_list, msg=("Excepted %s, got %s" % (excepted_list, res)))


if __name__ == "__main__":
    # create the test suit from the cases above.
    dayLightSuit = unittest.TestLoader().loadTestsFromTestCase(TestDaylightLength)
    sunHoursSuit = unittest.TestLoader().loadTestsFromTestCase(TestSunHours)
    # this will run the test suit
    unittest.TextTestRunner(verbosity=2).run(sunHoursSuit)
    unittest.TextTestRunner(verbosity=2).run(dayLightSuit)
