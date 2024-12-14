from typing import Optional


class Triangle:
    def __init__(
        self,
        base: float,
        height: float,
        side_a: Optional[float] = None,
        side_b: Optional[float] = None,
        side_c: Optional[float] = None,
    ):
        if not isinstance(base, (int, float)):
            raise TypeError("Base must be a number.")
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number.")
        if base < 0:
            raise ValueError("Base cannot be negative.")
        if height < 0:
            raise ValueError("Height cannot be negative.")

        self.base = base
        self.height = height

        if side_a is not None and side_b is not None and side_c is not None:
            if not all(
                isinstance(side, (int, float)) for side in [side_a, side_b, side_c]
            ):
                raise TypeError("All sides must be numbers.")
            if side_a <= 0 or side_b <= 0 or side_c <= 0:
                raise ValueError("Sides must be positive.")
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            self.side_a = None
            self.side_b = None
            self.side_c = None

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def perimeter(self) -> float:
        if self.side_a is None or self.side_b is None or self.side_c is None:
            raise ValueError("All three sides must be provided to calculate perimeter.")
        return self.side_a + self.side_b + self.side_c


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
