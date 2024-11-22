# geometric_lib/calculate.py

from typing import Dict

def calculate_area(radius: float) -> float:
    """
    Вычисляет площадь круга по заданному радиусу.
    
    :param radius: Радиус круга
    :return: Площадь круга
    """
    area = 3.14 * radius ** 2
    return area

def calculate_perimeter(radius: float) -> float:
    """
    Вычисляет периметр (длину окружности) круга по заданному радиусу.
    
    :param radius: Радиус круга
    :return: Периметр круга
    """
    perimeter = 2 * 3.14 * radius
    return perimeter

def create_shape_dict(name: str, radius: float) -> Dict[str, float]:
    """
    Создаёт словарь с информацией о форме.
    
    :param name: Название формы
    :param radius: Радиус формы
    :return: Словарь с ключами 'name' и 'radius'
    """
    return {'name': name, 'radius': radius}

def update_shape_radius(shape: Dict[str, float], new_radius: float) -> None:
    """
    Обновляет радиус формы в словаре.
    
    :param shape: Словарь с информацией о форме
    :param new_radius: Новый радиус формы
    """
    shape['radius'] = new_radius
