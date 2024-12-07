import unittest
from geometric_lib.triangle import area, perimeter

class TestTriangle(unittest.TestCase):

    def test_perimeter_valid(self):
        # Arrange
        side1, side2, side3 = 3, 4, 5
        expected = 12

        # Act
        result = perimeter(side1, side2, side3)

        # Assert
        self.assertEqual(result, expected)

    def test_perimeter_invalid(self):
        # Arrange
        side1, side2, side3 = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(side1, side2, side3)

    def test_area_valid(self):
        # Arrange
        side1, side2, side3 = 3, 4, 5
        expected = 6.0  # Площадь треугольника 3-4-5

        # Act
        result = area(side1, side2, side3)

        # Assert
        self.assertAlmostEqual(result, expected, places=2)

    def test_area_invalid_negative_side(self):
        # Arrange
        side1, side2, side3 = -3, 4, 5

        # Act & Assert
        with self.assertRaises(ValueError):
            area(side1, side2, side3)

    def test_area_invalid_triangle(self):
        # Arrange
        side1, side2, side3 = 1, 2, 3  # Некорректный треугольник

        # Act & Assert
        with self.assertRaises(ValueError):
            area(side1, side2, side3)
