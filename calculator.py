import unittest

# Функция калькулятора
def calculator(a, b, operation):
    if operation == 'сложение':
        return a + b
    elif operation == 'вычитание':
        return a - b
    elif operation == 'умножение':
        return a * b
    elif operation == 'деление':
        if b != 0:
            return a / b
        else:
            return "нельзя делить на ноль"
    else:
        return "некорректная операция"

# Тесты для проверки работы калькулятора
class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculator(3, 2, 'сложение')
        self.assertEqual(result, 5)  # Проверяем, что 3 + 2 = 5

    def test_subtraction(self):
        result = calculator(5, 3, 'вычитание')
        self.assertEqual(result, 2)  # Проверяем, что 5 - 3 = 2

    def test_multiplication(self):
        result = calculator(4, 3, 'умножение')
        self.assertEqual(result, 12)  # Проверяем, что 4 * 3 = 12

    def test_division(self):
        result = calculator(10, 2, 'divide')
        self.assertEqual(result, 5)  # Проверяем, что 10 / 2 = 5

    def test_division_by_zero(self):
        result = calculator(10, 0, 'деление')
        self.assertEqual(result, "нельзя делить на ноль")  # Проверяем деление на 0

    def test_invalid_operation(self):
        result = calculator(10, 5, 'unknown')
        self.assertEqual(result, "некорректная операция")  # Проверяем некорректную операцию

# Запуск тестов
if __name__ == "__main__":
    unittest.main()
