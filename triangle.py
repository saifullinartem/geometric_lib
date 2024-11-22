# geometric_lib/triangle.py
import math


def area(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive numbers.")
    s = (a + b + c) / 2
    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides.")
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    """Вычисляет периметр треугольника."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive numbers.")
    return a + b + c
