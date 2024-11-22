# tests/test_calculate.py
import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):
    """Тесты для функции calc в модуле calculate."""

    def test_calc_circle_area(self):
        """Тестирование вычисления площади круга."""
        # Arrange
        fig = "circle"
        func = "area"
        size = [5]
        expected = 78.53981633974483  # π * 5^2

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected, places=4)

    def test_calc_square_perimeter(self):
        """Тестирование вычисления периметра квадрата."""
        # Arrange
        fig = "square"
        func = "perimeter"
        size = [4]
        expected = 16  # 4 * 4

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected)

    def test_calc_triangle_area(self):
        """Тестирование вычисления площади треугольника."""
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4, 5]
        expected = 6.0  # Площадь треугольника 3,4,5 по формуле Герона

        # Act
        result = calc(fig, func, size)

        # Assert
        self.assertAlmostEqual(result, expected, places=4)

    def test_calc_invalid_figure(self):
        """Тестирование обработки несуществующей фигуры."""
        # Arrange
        fig = "hexagon"
        func = "area"
        size = [6]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertIn("Figure 'hexagon' is not supported.", str(context.exception))

    def test_calc_invalid_function(self):
        """Тестирование обработки несуществующей функции."""
        # Arrange
        fig = "circle"
        func = "volume"
        size = [5]

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertIn("Function 'volume' is not supported.", str(context.exception))

    def test_calc_invalid_size(self):
        """Тестирование обработки неверного количества параметров."""
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4]  # Требуется 3 параметра

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)
        self.assertIn("expects 3 parameter(s)", str(context.exception))

    def test_calc_negative_size(self):
        """Тестирование обработки отрицательных значений параметров."""
        # Arrange
        fig = "circle"
        func = "area"
        size = [-5]

        # Act & Assert
        with self.assertRaises(ValueError):
            calc(fig, func, size)


if __name__ == "__main__":
    unittest.main()
