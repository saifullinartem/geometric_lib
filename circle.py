# circle.py
import math

class Circle:
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь круга.
        """
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """
        Вычисляет периметр круга.
        """
        return 2 * math.pi * self.radius
