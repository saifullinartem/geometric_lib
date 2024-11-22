# tests/test_triangle.py
import unittest
import math
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    """Тесты для модуля triangle."""

    def test_perimeter_positive_sides(self):
        """Тестирование вычисления периметра треугольника с положительными сторонами."""
        # Arrange
        a, b, c = 3, 4, 5
        expected_perimeter = a + b + c

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_negative_side(self):
        """Тестирование обработки отрицательных сторон при вычислении периметра."""
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_area_positive_sides(self):
        """Тестирование вычисления площади треугольника с положительными сторонами."""
        # Arrange
        a, b, c = 3, 4, 5
        s = (a + b + c) / 2
        expected_area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Act
        result = area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=4)

    def test_area_invalid_sides(self):
        """Тестирование обработки некорректных сторон, не образующих треугольник."""
        # Arrange
        a, b, c = 1, 2, 3  # Не образуют треугольник

        # Act & Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_area_negative_side(self):
        """Тестирование обработки отрицательных сторон при вычислении площади."""
        # Arrange
        a, b, c = 3, -4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            area(a, b, c)


if __name__ == "__main__":
    unittest.main()
