import unittest # noqa: F401
import math # noqa: F401
from geometric_lib import circle # noqa: F401


class TestCircle(unittest.TestCase):
    def test_area_positive_radius(self):
        # Arrange
        radius = 5
        expected_area = math.pi * radius ** 2

        # Act
        result = circle.area(radius)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=4)

    def test_area_negative_radius(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.area(radius)

    def test_perimeter_positive_radius(self):
        # Arrange
        radius = 3
        expected_perimeter = 2 * math.pi * radius

        # Act
        result = circle.perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected_perimeter, places=4)

    def test_perimeter_negative_radius(self):
        # Arrange
        radius = -3

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.perimeter(radius)
