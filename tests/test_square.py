# tests/test_square.py
import pytest
from square import square

# Тест для периметра квадрата
def test_square_perimeter():
    assert square.perimeter(4) == 16

# Тест для площади квадрата
def test_square_area():
    assert square.area(4) == 16

# Тест для некорректных данных (отрицательная сторона)
def test_square_invalid_input():
    with pytest.raises(TypeError):
        square.perimeter(-4)

    with pytest.raises(TypeError):
        square.area(-4)
