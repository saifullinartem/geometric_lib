# geometric_lib/circle.py

def area(radius: float) -> float:
    """
    Вычисляет площадь круга.

    :param radius: Радиус круга
    :return: Площадь круга
    """
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return 3.14 * radius ** 2

def perimeter(radius: float) -> float:
    """
    Вычисляет периметр круга.

    :param radius: Радиус круга
    :return: Периметр круга
    """
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return 2 * 3.14 * radius
