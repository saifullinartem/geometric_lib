
import pytest
from circle import Circle

def test_circle_perimeter():
    radius = 3
    circle = Circle(radius=radius)
    expected_perimeter = 2 * 3.141592653589793 * radius  

    calculated_perimeter = circle.perimeter()

    assert calculated_perimeter == pytest.approx(expected_perimeter, rel=1e-9), \
        f"Expected perimeter {expected_perimeter}, got {calculated_perimeter}"

def test_circle_area():
    radius = 3
    circle = Circle(radius=radius)
    expected_area = 3.141592653589793 * radius ** 2  

    calculated_area = circle.area()

    assert calculated_area == pytest.approx(expected_area, rel=1e-9), \
        f"Expected area {expected_area}, got {calculated_area}"

def test_circle_invalid_input():
    invalid_radius = -3

    with pytest.raises(ValueError):
        Circle(radius=invalid_radius).perimeter()

    with pytest.raises(ValueError):
        Circle(radius=invalid_radius).area()
