class Square:
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number.")
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length


def area(side: float) -> float:
    """
    Вычисляет площадь квадрата.

    :param side: Длина стороны квадрата
    :return: Площадь квадрата
    """
    if side < 0:
        raise ValueError("Side length must be a non-negative number.")
    return side**2

    def area(self):
        return self.side_length**2
