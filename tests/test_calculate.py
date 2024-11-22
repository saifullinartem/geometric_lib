import unittest
from geometric_lib import calculate

class TestCalculate(unittest.TestCase):
    def test_calc_circle_area(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [5]
        expected = 78.53981633974483  # π * 5^2

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected, places=4)

    def test_calc_square_perimeter(self):
        # Arrange
        fig = 'square'
        func = 'perimeter'
        size = [4]
        expected = 16

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected)

    def test_calc_triangle_area(self):
        # Arrange
        fig = 'triangle'
        func = 'area'
        size = [3, 4, 5]
        expected = 6.0  # Площадь треугольника 3,4,5 по формуле Герона

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected, places=4)

    def test_calc_invalid_figure(self):
        # Arrange
        fig = 'hexagon'
        func = 'area'
        size = [6]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calculate.calc(fig, func, size)
        self.assertIn("Figure 'hexagon' is not supported.", str(context.exception))

    def test_calc_invalid_function(self):
        # Arrange
        fig = 'circle'
        func = 'volume'
        size = [5]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calculate.calc(fig, func, size)
        self.assertIn("Function 'volume' is not supported.", str(context.exception))

    def test_calc_invalid_size(self):
        # Arrange
        fig = 'triangle'
        func = 'area'
        size = [3, 4]  # Требуется 3 параметра

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calculate.calc(fig, func, size)
        self.assertIn("expects 3 parameter(s)", str(context.exception))

    def test_calc_negative_size(self):
        # Arrange
        fig = 'circle'
        func = 'area'
        size = [-5]

        # Act & Assert
        with self.assertRaises(ValueError):
            calculate.calc(fig, func, size)
