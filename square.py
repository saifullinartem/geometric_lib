
class Square:
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number.")
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

    def area(self):
        return self.side_length ** 2
