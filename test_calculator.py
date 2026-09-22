import unittest
from calculator import add, multiply

class CalculatorTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)
    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 3), -6)
    def test_multiply_zero(self):
        self.assertEqual(multiply(7, 0), 0)
