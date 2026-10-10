import unittest
from calculator import add, square

class CalculatorTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
    def test_square_positive(self):
        self.assertEqual(square(3), 9)
    def test_square_negative(self):
        self.assertEqual(square(-4), 16)
    def test_square_zero(self):
        self.assertEqual(square(0), 0)
