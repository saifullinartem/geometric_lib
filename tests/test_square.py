

import pytest
from square import Square

def test_square_area():
    # Arrange
    side_length = 4
    square = Square(side_length=side_length)
    expected_area = side_length ** 2  # 16

    # Act
    calculated_area = square.area()

    # Assert
    assert calculated_area == expected_area, f"Expected area {expected_area}, got {calculated_area}"

def test_square_perimeter():
    # Arrange
    side_length = 5
    square = Square(side_length=side_length)
    expected_perimeter = 4 * side_length  # 20

    # Act
    calculated_perimeter = square.perimeter()

    # Assert
    assert calculated_perimeter == expected_perimeter, f"Expected perimeter {expected_perimeter}, got {calculated_perimeter}"

def test_square_invalid_input():
    # Arrange
    with pytest.raises(ValueError):
        Square(side_length=-4)

    with pytest.raises(TypeError):
        Square(side_length="five")
