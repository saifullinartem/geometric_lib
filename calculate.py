import math
from .circle import area as circle_area, perimeter as circle_perimeter
from .square import area as square_area, perimeter as square_perimeter
from .triangle import area as triangle_area, perimeter as triangle_perimeter

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
    shape = args.get('shape')
    if shape == 'circle':
        radius = args.get('radius')
        if radius is None:
            raise ValueError("Radius is required for circle.")
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return {
            'area': circle_area(radius),
            'perimeter': circle_perimeter(radius)
        }
    elif shape == 'square':
        side = args.get('side')
        if side is None:
            raise ValueError("Side is required for square.")
        if side < 0:
            raise ValueError("Side cannot be negative.")
        return {
            'area': square_area(side),
            'perimeter': square_perimeter(side)
        }
    elif shape == 'triangle':
        side1 = args.get('side1')
        side2 = args.get('side2')
        side3 = args.get('side3')
        if None in (side1, side2, side3):
            raise ValueError("All three sides are required for triangle.")
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("Sides cannot be negative.")
        return {
            'area': triangle_area(side1, side2, side3),
            'perimeter': triangle_perimeter(side1, side2, side3)
        }
    else:
        raise ValueError(f"Unknown shape: {shape}")
