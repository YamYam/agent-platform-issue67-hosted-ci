import unittest
from calculator import add, cube

class CalculatorTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
    def test_cube_positive(self):
        self.assertEqual(cube(2), 8)
    def test_cube_negative(self):
        self.assertEqual(cube(-3), -27)
    def test_cube_zero(self):
        self.assertEqual(cube(0), 0)
    def test_cube_positive_eleven(self):
        self.assertEqual(cube(11), 1331)
    def test_cube_negative_eleven(self):
        self.assertEqual(cube(-11), -1331)
