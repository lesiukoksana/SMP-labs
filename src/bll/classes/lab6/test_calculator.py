import unittest
import math
from src.bll.functions.lab1.functions import calculateExpression

class UnitTestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculateExpression(5, 3, '+'), 8)
        self.assertEqual(calculateExpression(-5, 3, '+'), -2)
        self.assertEqual(calculateExpression(-5, -3, '+'), -8)

    def test_subtraction(self):
        self.assertEqual(calculateExpression(5, 3, '-'), 2)
        self.assertEqual(calculateExpression(3, 5, '-'), -2)
        self.assertEqual(calculateExpression(-5, -3, '-'), -2)

    def test_multiplication(self):
        self.assertEqual(calculateExpression(5, 3, '*'), 15)
        self.assertEqual(calculateExpression(5, 0, '*'), 0)
        self.assertEqual(calculateExpression(-5, 3, '*'), -15)
        self.assertEqual(calculateExpression(-5, -3, '*'), 15)

    def test_division(self):
        self.assertEqual(calculateExpression(6, 3, '/'), 2)
        self.assertEqual(calculateExpression(-6, 3, '/'), -2)
        self.assertIsNone(calculateExpression(6, 0, '/'), "You cannot divide by zero!")

    def test_error_handling(self):
        self.assertIsNone(calculateExpression(6, 0, '/'), "You cannot divide by zero!")
        self.assertIsNone(calculateExpression(-9, None, '√'), "Number cannot be lower than zero!")

if __name__ == '__main__':
    unittest.main()

