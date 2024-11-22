import unittest
from geometric_lib.calculate import calculate_area, calculate_perimeter

class TestCalculate(unittest.TestCase):
    def test_calculate_area(self):
        self.assertEqual(calculate_area(5), 78.5)
        self.assertEqual(calculate_area(0), 0)
        self.assertAlmostEqual(calculate_area(3.5), 38.465)

    def test_calculate_perimeter(self):
        self.assertEqual(calculate_perimeter(5), 31.4)
        self.assertEqual(calculate_perimeter(0), 0)
        self.assertAlmostEqual(calculate_perimeter(3.5), 21.98)

if __name__ == '__main__':
    unittest.main()
