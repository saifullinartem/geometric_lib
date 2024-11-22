# tests/test_square.py
import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    """Тесты для модуля square."""

    def test_area_positive_side(self):
        """Тестирование вычисления площади квадрата с положительной стороной."""
        # Arrange
        side = 4
        expected_area = side * side

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, expected_area)

    def test_area_negative_side(self):
        """Тестирование обработки отрицательной стороны при вычислении площади."""
        # Arrange
        side = -4

        # Act & Assert
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_positive_side(self):
        """Тестирование вычисления периметра квадрата с положительной стороной."""
        # Arrange
        side = 3
        expected_perimeter = 4 * side

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_negative_side(self):
        """Тестирование обработки отрицательной стороны при вычислении периметра."""
        # Arrange
        side = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == '__main__':
    unittest.main()
