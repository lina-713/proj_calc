import unittest
import math

class Calculator:
    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2

    def sin(self, num):
        return math.sin(num)

    def cos(self, num):
        return math.cos(num)

    def sqrt(self, num):
        return math.sqrt(num)

    def floor(self, num):
        return math.floor(num)

    def ceil(self, num):
        return math.ceil(num)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.addition(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calculator.subtraction(5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calculator.multiplication(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.calculator.division(6, 2)
        self.assertEqual(result, 3)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            self.calculator.division(6, 0)

    def test_sin(self):
        result = self.calculator.sin(math.pi / 2)
        self.assertAlmostEqual(result, 1.0)

    def test_cos(self):
        result = self.calculator.cos(0)
        self.assertAlmostEqual(result, 1.0)

    def test_sqrt(self):
        result = self.calculator.sqrt(9)
        self.assertAlmostEqual(result, 3.0)

    def test_floor(self):
        result = self.calculator.floor(3.5)
        self.assertEqual(result, 3)

    def test_ceil(self):
        result = self.calculator.ceil(3.2)
        self.assertEqual(result, 4)
#доделала
if __name__ == '__main__':
    unittest.main()
