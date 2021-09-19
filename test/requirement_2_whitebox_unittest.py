from app.calculator import *
import unittest
from datetime import date, time

class SolarEnergyPastCalculator:

    def __init__(self):
        self.calculator = Calculator()
        self.postcode = "4000"
