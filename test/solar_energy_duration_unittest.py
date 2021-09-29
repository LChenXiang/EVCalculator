from app.calculator import *
import unittest
from datetime import date, time

class TestSolarEnergyDuration(unittest.TestCase):
    # t1- error , t2-start>sunset, t3-normal
    def setUp(self) -> None:
        self.calculator = Calculator()