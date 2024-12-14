import math


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")


def area(radius: float) -> float:
    """
    Вычисляет площадь круга.
    :param radius: Радиус круга
    :return: Площадь круга
    """
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return math.pi * radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2
