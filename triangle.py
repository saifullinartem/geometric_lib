import math

def perimeter(side1: float, side2: float, side3: float) -> float:
    """
    Вычисляет периметр треугольника.
    :param side1: Первая сторона
    :param side2: Вторая сторона
    :param side3: Третья сторона
    :return: Периметр треугольника
    """
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("Sides must be non-negative numbers.")
    return side1 + side2 + side3

def area(side1: float, side2: float, side3: float) -> float:
    """
    Вычисляет площадь треугольника по трем сторонам (формула Герона).
    :param side1: Первая сторона
    :param side2: Вторая сторона
    :param side3: Третья сторона
    :return: Площадь треугольника
    """
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("Sides must be non-negative numbers.")
    # Проверка существования треугольника по неравенству треугольника
    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        raise ValueError("The given sides do not form a valid triangle.")
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
