import math
import unittest

# Функция для решения квадратного уравнения
def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c  # Вычисляем дискриминант
    if discriminant < 0:
        return None  # Нет корней (уравнение не имеет решений)
    elif discriminant == 0:
        return -b / (2 * a)  # Один корень
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)  # Первый корень
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)  # Второй корень
        return root1, root2  # Два корня

# Тесты для проверки работы функции
class TestQuadratic(unittest.TestCase):

    def test_two_roots(self):
        # Проверим уравнение: x^2 - 5x + 6 = 0
        result = solve_quadratic(1, -5, 6)
        self.assertEqual(result, (3, 2))  # Ожидаем, что корни будут 3 и 2

    def test_one_root(self):
        # Проверим уравнение: x^2 - 4x + 4 = 0
        result = solve_quadratic(1, -4, 4)
        self.assertEqual(result, 2)  # Ожидаем один корень: 2

    def test_no_roots(self):
        # Проверим уравнение: x^2 + x + 1 = 0
        result = solve_quadratic(1, 1, 1)
        self.assertIsNone(result)  # Ожидаем отсутствие корней (None)

# Это нужно для запуска тестов, когда файл выполняется напрямую
if __name__ == "__main__":
    unittest.main()
