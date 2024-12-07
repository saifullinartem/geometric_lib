# tests/test_triangle.py

import pytest
from triangle import Triangle

def test_triangle_area():
    # Arrange
    base = 4
    height = 3
    triangle = Triangle(base=base, height=height)
    expected_area = 0.5 * base * height  # 6

    # Act
    calculated_area = triangle.area()

    # Assert
    assert calculated_area == expected_area, f"Expected area {expected_area}, got {calculated_area}"

def test_triangle_perimeter():
    # Arrange
    side_a = 3
    side_b = 4
    side_c = 5
    triangle = Triangle(base=side_a, height=side_b, side_a=side_a, side_b=side_b, side_c=side_c)
    expected_perimeter = side_a + side_b + side_c  # 12

    # Act
    calculated_perimeter = triangle.perimeter()

    # Assert
    assert calculated_perimeter == expected_perimeter, f"Expected perimeter {expected_perimeter}, got {calculated_perimeter}"

def test_triangle_invalid_input():
    # Arrange & Act & Assert
    with pytest.raises(ValueError):
        Triangle(base=-4, height=3)

    with pytest.raises(ValueError):
        Triangle(base=4, height=-3)

    with pytest.raises(ValueError):
        Triangle(base=3, height=4, side_a=-5, side_b=4, side_c=5)

    with pytest.raises(TypeError):
        Triangle(base="four", height=3)

    with pytest.raises(TypeError):
        Triangle(base=3, height=4, side_a="five", side_b=4, side_c=5)
