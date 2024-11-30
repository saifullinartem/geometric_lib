# geometric_lib/calculate.py

from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter

def calculate_area(radius: float) -> float:
    """
    Вычисляет площадь круга по заданному радиусу.

    :param radius: Радиус круга
    :return: Площадь круга
    """
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return circle_area(radius)

def calculate_perimeter(radius: float) -> float:
    """
    Вычисляет периметр (длину окружности) круга по заданному радиусу.

    :param radius: Радиус круга
    :return: Периметр круга
    """
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return circle_perimeter(radius)
