import unittest
import math
import tkinter as tk
from tkinter import Tk
from tkinter.messagebox import _show
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.root.withdraw() 
    def tearDown(self):
        self.root.destroy()

    def test_addition(self):
        result = self.calculate_operation("Сложение", 2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calculate_operation("Вычитание", 5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calculate_operation("Умножение", 2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.calculate_operation("Деление", 6, 2)
        self.assertEqual(result, 3)

    def test_zero_division(self):
        with self.assertRaises(tk.TclError):  
            self.calculate_operation("Деление", 6, 0)

    def test_sin(self):
        result = self.calculate_operation("Sin", math.pi / 2, 0)
        self.assertAlmostEqual(result, 1.0)

    def test_cos(self):
        result = self.calculate_operation("Cos", 0, 0)
        self.assertAlmostEqual(result, 1.0)

    def test_sqrt(self):
        result = self.calculate_operation("Квадратный корень", 9, 0)
        self.assertAlmostEqual(result, 3.0)

    def test_floor(self):
        result = self.calculate_operation("Округление в меньшую сторону", 3.5, 0)
        self.assertEqual(result, 3)

    def test_ceil(self):
        result = self.calculate_operation("Округление в большую сторону", 3.2, 0)
        self.assertEqual(result, 4)

    def calculate_operation(self, operation, num1, num2):
        entry_num1 = num1
        entry_num2 = num2

        if operation == "Деление" and num2 == 0:
            raise tk.TclError("Деление на ноль невозможно")

        if operation == "Сложение":
            result = num1 + num2
        elif operation == "Вычитание":
            result = num1 - num2
        elif operation == "Умножение":
            result = num1 * num2
        elif operation == "Деление":
            result = num1 / num2
        elif operation == "Остаток от деления":
            result = num1 % num2
        elif operation == "Возведение в степень":
            result = num1 ** num2
        elif operation == "Sin":
            result = math.sin(num1)
        elif operation == "Cos":
            result = math.cos(num1)
        elif operation == "Квадратный корень":
            result = math.sqrt(num1)
        elif operation == "Округление в меньшую сторону":
            result = math.floor(num1)
        elif operation == "Округление в большую сторону":
            result = math.ceil(num1)

        return result


if __name__ == '__main__':
    unittest.main(exit=False)