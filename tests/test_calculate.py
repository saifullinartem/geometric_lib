# tests/test_calculate.py
import pytest
import math
from calculate import Calculator, calculate_area, calculate_perimeter, calc

@pytest.fixture
def calculator():
    return Calculator()

def test_calculator_add(calculator):
    a = 2
    b = 3
    expected = 5
    result = calculator.add(a, b)
    assert result == expected, f"Expected {expected}, got {result}"

def test_calculate_area_valid_circle():
    # Arrange
    input_data = {"shape": "circle", "radius": 5}
    expected = math.pi * 5**2  # Площадь круга с радиусом 5

    # Act
    result = calculate_area(input_data["radius"])

    # Assert
    assert result == pytest.approx(expected, rel=1e-9), f"Expected {expected}, got {result}"

def test_calculator_subtract(calculator):
    a = 5
    b = 3
    expected = 2
    result = calculator.subtract(a, b)
    assert result == expected, f"Expected {expected}, got {result}"

def test_calculator_multiply(calculator):
    a = 4
    b = 3
    expected = 12
    result = calculator.multiply(a, b)
    assert result == expected, f"Expected {expected}, got {result}"

def test_calculate_area_invalid_circle():
    # Arrange
    input_data = {"shape": "circle", "radius": -5}

    # Act & Assert
    with pytest.raises(ValueError):
        calculate_area(input_data["radius"])

def test_calculate_perimeter_valid_circle():
    # Arrange
    input_data = {"shape": "circle", "radius": 3}
    expected = 2 * math.pi * 3  # Периметр круга с радиусом 3

    # Act
    result = calculate_perimeter(input_data["radius"])

    # Assert
    assert result == pytest.approx(expected, rel=1e-9), f"Expected {expected}, got {result}"

def test_calculator_divide(calculator):
    a = 10
    b = 2
    expected = 5
    result = calculator.divide(a, b)
    assert result == expected, f"Expected {expected}, got {result}"

def test_calculate_perimeter_invalid_circle():
    # Arrange
    input_data = {"shape": "circle", "radius": -3}

    # Act & Assert
    with pytest.raises(ValueError):
        calculate_perimeter(input_data["radius"])

def test_calc_valid_input_circle():
    # Arrange
    args = {"shape": "circle", "radius": 3}
    expected = {"area": math.pi * 3**2, "perimeter": 2 * math.pi * 3}

    # Act
    result = calc(args)

    # Assert
    assert result["area"] == pytest.approx(expected["area"], rel=1e-9), \
        f"Expected area {expected['area']}, got {result['area']}"
    assert result["perimeter"] == pytest.approx(expected["perimeter"], rel=1e-9), \
        f"Expected perimeter {expected['perimeter']}, got {result['perimeter']}"

def test_calculator_divide_by_zero(calculator):
    a = 10
    b = 0
    with pytest.raises(ValueError):
        calculator.divide(a, b)

def test_calc_invalid_input_circle_negative_radius():
    # Arrange
    args = {"shape": "circle", "radius": -3}

    # Act & Assert
    with pytest.raises(ValueError):
        calc(args)

def test_calculator_invalid_input(calculator):
    with pytest.raises(TypeError):
        calculator.add("two", 3)
    with pytest.raises(TypeError):
        calculator.subtract(5, None)
    with pytest.raises(TypeError):
        calculator.multiply(4, "three")
    with pytest.raises(TypeError):
        calculator.divide("ten", 2)

def test_calc_valid_input_triangle():
    # Arrange
    args = {"shape": "triangle", "side1": 3, "side2": 4, "side3": 5}
    expected_area = 6.0  # Площадь треугольника 3-4-5
    expected_perimeter = 12.0

    # Act
    result = calc(args)

    # Assert
    assert result["area"] == pytest.approx(expected_area, rel=1e-9), \
        f"Expected area {expected_area}, got {result['area']}"
    assert result["perimeter"] == pytest.approx(expected_perimeter, rel=1e-9), \
        f"Expected perimeter {expected_perimeter}, got {result['perimeter']}"

def test_calc_invalid_input_triangle():
    # Arrange
    args = {
        "shape": "triangle",
        "side1": 1,
        "side2": 2,
        "side3": 3,
    }  # Некорректный треугольник

    # Act & Assert
    with pytest.raises(ValueError):
        calc(args)
