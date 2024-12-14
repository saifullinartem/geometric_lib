# calculate.py
import math

class Calculator:
    def add(self, a, b):
        """Возвращает сумму двух чисел."""
        return a + b

    def subtract(self, a, b):
        """Возвращает разность двух чисел."""
        return a - b

    def multiply(self, a, b):
        """Возвращает произведение двух чисел."""
        return a * b

    def divide(self, a, b):
        """Возвращает частное двух чисел. Выбрасывает ValueError при делении на ноль."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

def circle_area(radius: float) -> float:
    """
    Вычисляет площадь круга.
    """
    return math.pi * radius ** 2

def circle_perimeter(radius: float) -> float:
    """
    Вычисляет периметр круга.
    """
    return 2 * math.pi * radius

def square_area(side: float) -> float:
    """
    Вычисляет площадь квадрата.
    """
    return side ** 2

def square_perimeter(side: float) -> float:
    """
    Вычисляет периметр квадрата.
    """
    return 4 * side

def triangle_area(side1: float, side2: float, side3: float) -> float:
    """
    Вычисляет площадь треугольника по формуле Герона.
    """
    s = (side1 + side2 + side3) / 2
    area_squared = s * (s - side1) * (s - side2) * (s - side3)
    if area_squared <= 0:
        raise ValueError("Invalid triangle sides.")
    return math.sqrt(area_squared)

def triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    """
    Вычисляет периметр треугольника.
    """
    return side1 + side2 + side3

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

def calc(args: dict) -> dict:
    """
    Расчитывает площадь и периметр заданной геометрической фигуры.
    :param args: Словарь с параметрами фигуры.
    :return: Словарь с ключами 'area' и 'perimeter'.
    """
    shape = args.get("shape")
    if shape == "circle":
        radius = args.get("radius")
        if radius is None:
            raise ValueError("Radius is required for circle.")
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return {"area": circle_area(radius), "perimeter": circle_perimeter(radius)}
    elif shape == "square":
        side = args.get("side")
        if side is None:
            raise ValueError("Side is required for square.")
        if side < 0:
            raise ValueError("Side cannot be negative.")
        return {"area": square_area(side), "perimeter": square_perimeter(side)}
    elif shape == "triangle":
        side1 = args.get("side1")
        side2 = args.get("side2")
        side3 = args.get("side3")
        if None in (side1, side2, side3):
            raise ValueError("All three sides are required for triangle.")
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("Sides cannot be negative.")
        return {
            "area": triangle_area(side1, side2, side3),
            "perimeter": triangle_perimeter(side1, side2, side3),
        }
    else:
        raise ValueError(f"Unsupported shape: {shape}")
