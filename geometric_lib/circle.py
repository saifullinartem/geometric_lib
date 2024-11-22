# geometric_lib/circle.py
import math


def area(radius):
    """Вычисляет площадь круга."""
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return math.pi * radius**2


def perimeter(radius):
    """Вычисляет периметр круга."""
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return 2 * math.pi * radius
