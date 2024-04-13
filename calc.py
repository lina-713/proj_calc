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

    # Создание основного окна


root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x300")  # Установка размеров окна

# Выбор операции
operation_var = tk.StringVar(root)
operations = [
    "Сложение", "Вычитание", "Умножение", "Деление",
    "Остаток от деления", "Sin", "Cos", "Возведение в степень",
    "Квадратный корень", "Округление в меньшую сторону",
    "Округление в большую сторону"
]
operation_var.set(operations[0])
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=5)

# Поля для ввода чисел
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

# Кнопка "Выбор операции"
select_operation_button = tk.Button(root, text="Выбрать операцию", command=show_input_fields)
select_operation_button.pack(pady=5)

# Кнопка "Вычислить"
calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack(pady=10)

# Поле для вывода результата
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()