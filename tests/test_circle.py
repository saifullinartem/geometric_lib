# tests/test_circle.py
import pytest
import math
from circle import Circle


@pytest.fixture
def circle():
    return Circle(radius=5)


def test_circle_perimeter():
    radius = 3
    circle = Circle(radius=radius)
    expected_perimeter = 2 * math.pi * radius
    calculated_perimeter = circle.perimeter()
    assert calculated_perimeter == pytest.approx(
        expected_perimeter, rel=1e-9
    ), f"Expected perimeter {expected_perimeter}, got {calculated_perimeter}"


def test_area_positive_radius():
    # Arrange
    radius = 3
    expected = math.pi * radius**2  # Площадь круга с радиусом 3

    # Act
    circle = Circle(radius=radius)
    calculated_area = circle.area()

    # Assert
    assert calculated_area == pytest.approx(
        expected, rel=1e-9
    ), f"Expected area {expected}, got {calculated_area}"


def test_circle_area():
    radius = 3
    circle = Circle(radius=radius)
    expected_area = math.pi * radius**2

    calculated_area = circle.area()

    assert calculated_area == pytest.approx(
        expected_area, rel=1e-9
    ), f"Expected area {expected_area}, got {calculated_area}"


def test_circle_invalid_input():
    invalid_radius = -3

    with pytest.raises(ValueError):
        Circle(radius=invalid_radius).perimeter()

    with pytest.raises(ValueError):
        Circle(radius=invalid_radius).area()
