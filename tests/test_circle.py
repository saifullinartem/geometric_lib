# tests/test_circle.py
import unittest
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):
    """Тесты для модуля circle."""

    def test_area_positive_radius(self):
        """Тестирование вычисления площади круга с положительным радиусом."""
        # Arrange
        radius = 5
        expected_area = math.pi * radius ** 2

        # Act
        result = area(radius)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=4)

    def test_area_negative_radius(self):
        """Тестирование обработки отрицательного радиуса при вычислении площади."""
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            area(radius)

    def test_perimeter_positive_radius(self):
        """Тестирование вычисления периметра круга с положительным радиусом."""
        # Arrange
        radius = 3
        expected_perimeter = 2 * math.pi * radius

        # Act
        result = perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected_perimeter, places=4)

    def test_perimeter_negative_radius(self):
        """Тестирование обработки отрицательного радиуса при вычислении периметра."""
        # Arrange
        radius = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(radius)


if __name__ == '__main__':
    unittest.main()
