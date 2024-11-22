# geometric_lib/square.py


def area(side):
    """Вычисляет площадь квадрата."""
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return side * side


def perimeter(side):
    """Вычисляет периметр квадрата."""
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return 4 * side
