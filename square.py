# geometric_lib/square.py

def area(side: float) -> float:
    """
    Вычисляет площадь квадрата.

    :param side: Длина стороны квадрата
    :return: Площадь квадрата
    """
    if side < 0:
        raise ValueError("Side length must be a non-negative number.")
    return side ** 2

def perimeter(side: float) -> float:
    """
    Вычисляет периметр квадрата.

    :param side: Длина стороны квадрата
    :return: Периметр квадрата
    """
    if side < 0:
        raise ValueError("Side length must be a non-negative number.")
    return 4 * side
