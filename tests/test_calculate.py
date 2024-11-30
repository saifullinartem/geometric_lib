# tests/test_calculate.py

import unittest
from calculate import calculate_area, calculate_perimeter

class TestCalculate(unittest.TestCase):
    def test_calculate_area_positive_radius(self):
        self.assertAlmostEqual(calculate_area(5), 78.5)
        self.assertAlmostEqual(calculate_area(3.5), 38.465)
    
    def test_calculate_area_zero_radius(self):
        self.assertEqual(calculate_area(0), 0)
    
    def test_calculate_area_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_area(-1)
    
    def test_calculate_perimeter_positive_radius(self):
        self.assertAlmostEqual(calculate_perimeter(5), 31.4)
        self.assertAlmostEqual(calculate_perimeter(3.5), 21.98)
    
    def test_calculate_perimeter_zero_radius(self):
        self.assertEqual(calculate_perimeter(0), 0)
    
    def test_calculate_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(-1)

if __name__ == '__main__':
    unittest.main()
