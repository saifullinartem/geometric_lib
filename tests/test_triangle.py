import unittest
import math
from geometric_lib import triangle

class TestTriangle(unittest.TestCase):
    def test_perimeter_positive_sides(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected_perimeter = a + b + c

        # Act
        result = triangle.perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_negative_side(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.perimeter(a, b, c)

    def test_area_positive_sides(self):
        # Arrange
        a, b, c = 3, 4, 5
        s = (a + b + c) / 2
        expected_area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Act
        result = triangle.area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=4)

    def test_area_invalid_sides(self):
        # Arrange
        a, b, c = 1, 2, 3  # Не образуют треугольник

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.area(a, b, c)

    def test_area_negative_side(self):
        # Arrange
        a, b, c = 3, -4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.area(a, b, c)
