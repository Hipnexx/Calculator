import pytest
import requests
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 3, 1) == 2

    def test_adding_correctly(self):
        assert self.calc.adding(self, 3, 1) == 4
