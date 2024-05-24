#!/bin/bash

# Загрузка актуального состояния с сервера
echo "Downloading the latest code from the server..."
git pull

# Сборка проекта
echo "Building the project..."
python setup.py build

# Запуск unittest
echo "Running unit tests..."
python unittest_calc.py

# Создание установщика
echo "Creating the installer..."
python setup.py bdist_wheel

# Установка 
echo "Installing the application..."
pip install dist/CalculatorApp-1.0-py3-none-any.whl

echo "Continuous Integration process completed successfully"
