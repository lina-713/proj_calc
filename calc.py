import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    operation = operation_var.get()
    
    if operation in ["Sin", "Cos", "Квадратный корень", "Округление в меньшую сторону", "Округление в большую сторону"]:
        num1 = float(entry_num1.get())
        if operation == "Sin":
            result = math.sin(num1)
        elif operation == "Cos":
            result = math.cos(num1)
        elif operation == "Квадратный корень":
            result = math.sqrt(num1)
        elif operation == "Округление в меньшую сторону":
            result = math.floor(num1)
        elif operation == "Округление в большую сторону":
            result = math.ceil(num1)
            
        result_label.config(text="Результат: " + str(result))
        
    else:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == "Деление" and num2 == 0:
            messagebox.showerror("Ошибка", "Деление на ноль невозможно")
            return
        
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
        
        result_label.config(text="Результат: " + str(result))

def show_input_fields():
    operation = operation_var.get()
    if operation in ["Sin", "Cos", "Квадратный корень", "Округление в меньшую сторону", "Округление в большую сторону"]:
        entry_num1.pack()
        entry_num2.pack_forget()
    else:
        entry_num1.pack()
        entry_num2.pack()

