import unittest
from calculator import add, subtract

class CalculatorTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)
    def test_subtract_negative(self):
        self.assertEqual(subtract(-2, 3), -5)
    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)
