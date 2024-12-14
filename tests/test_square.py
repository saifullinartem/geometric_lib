# tests/test_square.py
import pytest
from square import Square

@pytest.fixture
def square_instance():
    return Square(side_length=4)  # Вы можете изменить длину стороны по необходимости

def test_square_area():
    # Arrange
    side_length = 4
    square = Square(side_length=side_length)
    expected_area = side_length**2  # 16

    # Act
    calculated_area = square.area()

    # Assert
    assert calculated_area == pytest.approx(expected_area, rel=1e-9), \
        f"Expected area {expected_area}, got {calculated_area}"

def test_square_area_positive_side():
    square = Square(side_length=4)
    expected = 16
    result = square.area()
    assert result == expected, f"Expected {expected}, got {result}"

def test_square_area_zero_side():
    square = Square(side_length=0)
    expected = 0
    result = square.area()
    assert result == expected, f"Expected {expected}, got {result}"

def test_square_area_negative_side():
    with pytest.raises(ValueError):
        Square(side_length=-4)

def test_square_perimeter_positive_side():
    square = Square(side_length=4)
    expected = 16  # Периметр квадрата со стороной 4
    result = square.perimeter()
    assert result == expected, f"Expected {expected}, got {result}"

def test_square_perimeter_zero_side():
    square = Square(side_length=0)
    expected = 0
    result = square.perimeter()
    assert result == expected, f"Expected {expected}, got {result}"

def test_square_perimeter_negative_side():
    with pytest.raises(ValueError):
        Square(side_length=-4)
