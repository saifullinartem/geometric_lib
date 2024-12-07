# tests/test_triangle.py

import unittest
from geometric_lib.triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area_positive_base_height(self):
        self.assertEqual(area(5, 2), 5.0)
        self.assertEqual(area(3.5, 4), 7.0)
    
    def test_area_zero_base_height(self):
        self.assertEqual(area(0, 0), 0.0)
        self.assertEqual(area(0, 4), 0.0)
        self.assertEqual(area(3.5, 0), 0.0)
    
    def test_area_negative_base_height(self):
        with self.assertRaises(ValueError):
            area(-5, 2)
        with self.assertRaises(ValueError):
            area(5, -2)
        with self.assertRaises(ValueError):
            area(-5, -2)
    
    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(2.5, 3.5, 4.5), 10.5)
    
    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
    
    def test_perimeter_negative_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)
        with self.assertRaises(ValueError):
            perimeter(-3, -4, -5)

if __name__ == '__main__':
    unittest.main()
