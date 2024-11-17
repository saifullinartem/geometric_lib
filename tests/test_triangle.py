# tests/test_triangle.py
import pytest
from triangle import Triangle

# Тест для периметра треугольника
def test_triangle_perimeter():
    assert triangle.perimeter(3, 4, 5) == 12

# Тест для площади треугольника
def test_triangle_area():
    assert triangle.area(3, 4, 5) == 6.0

# Тест для некорректных данных для треугольника (невалидные стороны)
def test_invalid_triangle_perimeter():
    with pytest.raises(ValueError):
        triangle.perimeter(1, 2, 3)  # Не существует треугольника с такими сторонами

def test_invalid_triangle_area():
    with pytest.raises(ValueError):
        triangle.area(1, 2, 3)  # Не существует треугольника с такими сторонами

# Тест для треугольника с отрицательныp
def test_invalid_triangle_perimeter_negative_side():
    with pytest.raises(ValueError):
        calc('triangle', 'perimeter', [-3, 4, 5])  # Стороны не могут быть отрицательными

# Тест для треугольника с отрицательными сторонами (площадь)
def test_invalid_triangle_area_negative_side():
    with pytest.raises(ValueError):
        calc('triangle', 'area', [-3, 4, 5])  # Стороны не могут быть отрицательными

# Тест для треугольника с нулевыми сторонами (периметр)
def test_invalid_triangle_perimeter_zero_side():
    with pytest.raises(ValueError):
        calc('triangle', 'perimeter', [0, 4, 5])  # Стороны не могут быть нулевыми

# Тест для треугольника с нулевыми сторонами (площадь)
def test_invalid_triangle_area_zero_side():
    with pytest.raises(ValueError):
        calc('triangle', 'area', [0, 4, 5])  # Стороны не могут быть нулевыми

