import pytest
from calculate import Calculator


def test_calculator_add():
    calculator = Calculator()
    a = 2
    b = 3
    expected = 5

    result = calculator.add(a, b)


class TestCalculate():

    def test_calculate_area_valid_circle(self):
        # Arrange
        input_data = {"shape": "circle", "radius": 5}
        expected = math.pi * 5**2  # Площадь круга с радиусом 5

        # Act
        result = calculate_area(input_data["radius"])

    assert result == expected, f"Expected {expected}, got {result}"


def test_calculator_subtract():
    calculator = Calculator()
    a = 5
    b = 3
    expected = 2

    result = calculator.subtract(a, b)

    assert result == expected, f"Expected {expected}, got {result}"


def test_calculator_multiply():
    calculator = Calculator()
    a = 4
    b = 3
    expected = 12

    def test_calculate_area_invalid_circle(self):
        # Arrange
        input_data = {"shape": "circle", "radius": -5}

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_area(input_data["radius"])

    def test_calculate_perimeter_valid_circle(self):
        # Arrange
        input_data = {"shape": "circle", "radius": 3}
        expected = 2 * math.pi * 3  # Периметр круга с радиусом 3

        # Act
        result = calculate_perimeter(input_data["radius"])

    result = calculator.multiply(a, b)

    assert result == expected, f"Expected {expected}, got {result}"


def test_calculator_divide():
    calculator = Calculator()
    a = 10
    b = 2
    expected = 5

    result = calculator.divide(a, b)

    def test_calculate_perimeter_invalid_circle(self):
        # Arrange
        input_data = {"shape": "circle", "radius": -3}

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_perimeter(input_data["radius"])

    def test_calc_valid_input_circle(self):
        # Arrange
        args = {"shape": "circle", "radius": 3}
        expected = {"area": math.pi * 3**2, "perimeter": 2 * math.pi * 3}

    assert result == expected, f"Expected {expected}, got {result}"


def test_calculator_divide_by_zero():
    calculator = Calculator()
    a = 10
    b = 0

    with pytest.raises(ValueError):
        calculator.divide(a, b)

        # Assert
        self.assertAlmostEqual(result["area"], expected["area"], places=2)
        self.assertAlmostEqual(result["perimeter"], expected["perimeter"], places=2)

    def test_calc_invalid_input_circle_negative_radius(self):
        # Arrange
        args = {"shape": "circle", "radius": -3}


def test_calculator_invalid_input():
    calculator = Calculator()

    with pytest.raises(TypeError):
        calculator.add("two", 3)

    def test_calc_valid_input_triangle(self):
        # Arrange
        args = {"shape": "triangle", "side1": 3, "side2": 4, "side3": 5}
        expected_area = 6.0  # Площадь треугольника 3-4-5
        expected_perimeter = 12.0

    with pytest.raises(TypeError):
        calculator.subtract(5, None)

    with pytest.raises(TypeError):
        calculator.multiply(4, "three")

    with pytest.raises(TypeError):
        calculator.divide("ten", 2)
        # Assert
        self.assertAlmostEqual(result["area"], expected_area, places=2)
        self.assertAlmostEqual(result["perimeter"], expected_perimeter, places=2)

    def test_calc_invalid_input_triangle(self):
        # Arrange
        args = {
            "shape": "triangle",
            "side1": 1,
            "side2": 2,
            "side3": 3,
        }  # Некорректный треугольник

        # Act & Assert
        with self.assertRaises(ValueError):
            calc(args)
