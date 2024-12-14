# square.py
class Square:
    def __init__(self, side_length: float):
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side_length = side_length

    def area(self) -> float:
        """
        Вычисляет площадь квадрата.
        """
        return self.side_length ** 2

    def perimeter(self) -> float:
        """
        Вычисляет периметр квадрата.
        """
        return 4 * self.side_length
