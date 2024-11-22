# tests/test_square.py
import unittest
from geometric_lib import square

class TestSquare(unittest.TestCase):
    def test_area_positive_side(self):
        # Arrange
        side = 4
        expected_area = side * side

        # Act
        result = square.area(side)

        # Assert
        self.assertEqual(result, expected_area)

    def test_area_negative_side(self):
        # Arrange
        side = -4

        # Act & Assert
        with self.assertRaises(ValueError):
            square.area(side)

    def test_perimeter_positive_side(self):
        # Arrange
        side = 3
        expected_perimeter = 4 * side

        # Act
        result = square.perimeter(side)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_negative_side(self):
        # Arrange
        side = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            square.perimeter(side)
