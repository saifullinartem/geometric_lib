import unittest
import math
from calculate import calculate_area, calculate_perimeter, calc

class TestCalculate(unittest.TestCase):

    def test_calculate_area_valid_circle(self):
        # Arrange
        input_data = {'shape': 'circle', 'radius': 5}
        expected = math.pi * 5 ** 2  # Площадь круга с радиусом 5

        # Act
        result = calculate_area(input_data['radius'])

        # Assert
        self.assertAlmostEqual(result, expected, places=2)

    def test_calculate_area_invalid_circle(self):
        # Arrange
        input_data = {'shape': 'circle', 'radius': -5}

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_area(input_data['radius'])

    def test_calculate_perimeter_valid_circle(self):
        # Arrange
        input_data = {'shape': 'circle', 'radius': 3}
        expected = 2 * math.pi * 3  # Периметр круга с радиусом 3

        # Act
        result = calculate_perimeter(input_data['radius'])

        # Assert
        self.assertAlmostEqual(result, expected, places=2)

    def test_calculate_perimeter_invalid_circle(self):
        # Arrange
        input_data = {'shape': 'circle', 'radius': -3}

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate_perimeter(input_data['radius'])

    def test_calc_valid_input_circle(self):
        # Arrange
        args = {'shape': 'circle', 'radius': 3}
        expected = {
            'area': math.pi * 3 ** 2,
            'perimeter': 2 * math.pi * 3
        }

        # Act
        result = calc(args)

        # Assert
        self.assertAlmostEqual(result['area'], expected['area'], places=2)
        self.assertAlmostEqual(result['perimeter'], expected['perimeter'], places=2)

    def test_calc_invalid_input_circle_negative_radius(self):
        # Arrange
        args = {'shape': 'circle', 'radius': -3}

        # Act & Assert
        with self.assertRaises(ValueError):
            calc(args)

    def test_calc_valid_input_triangle(self):
        # Arrange
        args = {'shape': 'triangle', 'side1': 3, 'side2': 4, 'side3': 5}
        expected_area = 6.0  # Площадь треугольника 3-4-5
        expected_perimeter = 12.0

        # Act
        result = calc(args)

        # Assert
        self.assertAlmostEqual(result['area'], expected_area, places=2)
        self.assertAlmostEqual(result['perimeter'], expected_perimeter, places=2)

    def test_calc_invalid_input_triangle(self):
        # Arrange
        args = {'shape': 'triangle', 'side1': 1, 'side2': 2, 'side3': 3}  # Некорректный треугольник

        # Act & Assert
        with self.assertRaises(ValueError):
            calc(args)
