import unittest
import math
from .circle import area, perimeter

class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        # Arrange
        radius = 3
        expected = math.pi * radius ** 2  # Площадь круга с радиусом 3

        # Act
        result = area(radius)

        # Assert
        self.assertAlmostEqual(result, expected, places=2)

    def test_area_negative_radius(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            area(radius)

    def test_area_zero_radius(self):
        # Arrange
        radius = 0
        expected = 0.0

        # Act
        result = area(radius)

        # Assert
        self.assertEqual(result, expected)

    def test_perimeter_positive_radius(self):
        # Arrange
        radius = 3
        expected = 2 * math.pi * radius  # Периметр круга с радиусом 3

        # Act
        result = perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected, places=2)

    def test_perimeter_negative_radius(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(radius)

    def test_perimeter_zero_radius(self):
        # Arrange
        radius = 0
        expected = 0.0

        # Act
        result = perimeter(radius)

        # Assert
        self.assertEqual(result, expected)
