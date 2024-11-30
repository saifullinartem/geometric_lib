# geometric_lib/triangle.py

def area(base: float, height: float) -> float:
    """
    Вычисляет площадь треугольника.

    :param base: Основание треугольника
    :param height: Высота треугольника
    :return: Площадь треугольника
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative numbers.")
    return 0.5 * base * height

def perimeter(side1: float, side2: float, side3: float) -> float:
    """
    Вычисляет периметр треугольника.

    :param side1: Длина первой стороны
    :param side2: Длина второй стороны
    :param side3: Длина третьей стороны
    :return: Периметр треугольника
    """
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("All sides must be non-negative numbers.")
    return side1 + side2 + side3
