# tests/test_circle.py
import pytest
from circle import circle

# Тест для периметра круга
def test_circle_perimeter():
    assert circle.perimeter(3) == pytest.approx(18.84955592153876, rel=1e-9)

# Тест для площади круга
def test_circle_area():
    assert circle.area(3) == pytest.approx(28.274333882308138, rel=1e-9)

# Тест для некорректных данных (отрицательный радиус)
def test_circle_invalid_input():
    with pytest.raises(ValueError):
        circle.perimeter(-3)

    with pytest.raises(ValueError):
        circle.area(-3)
