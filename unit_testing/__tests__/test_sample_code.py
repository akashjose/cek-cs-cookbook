import unittest
from unit_testing.code.sample_code import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(10, -5), -2)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(5, 0), "Error: Division by zero!")
