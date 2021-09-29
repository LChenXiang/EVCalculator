from app.calculator import *
import unittest
from datetime import date, time

class TestSolarEnergyDuration(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()