import pytest
from square import Square


def test_square_area():
    # Arrange
    side_length = 4
    square = Square(side_length=side_length)
    expected_area = side_length**2  # 16

    # Act
    calculated_area = square.area()

    # Assert
    assert (
        calculated_area == expected_area
    ), f"Expected area {expected_area}, got {calculated_area}"


def test_square_perimeter():
    # Arrange
    side_length = 5
    square = Square(side_length=side_length)
    expected_perimeter = 4 * side_length  # 20

    # Act
    calculated_perimeter = square.perimeter()

    # Assert
    assert (
        calculated_perimeter == expected_perimeter
    ), f"Expected perimeter {expected_perimeter}, got {calculated_perimeter}"


def test_square_invalid_input():
    # Arrange
    with pytest.raises(ValueError):
        Square(side_length=-4)

    with pytest.raises(TypeError):
        Square(side_length="five")


class TestSquare(unittest.TestCase):
    def test_area_positive_side(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(2.5), 6.25)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(2.5), 10)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == "__main__":
    unittest.main()
