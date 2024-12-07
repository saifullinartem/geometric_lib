# tests/test_circle.py

import unittest
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(3), 28.26)
        self.assertAlmostEqual(area(2.5), 19.625)
    
    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)
    
    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-3)
    
    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(3), 18.84)
        self.assertAlmostEqual(perimeter(2.5), 15.7)
    
    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-3)

if __name__ == '__main__':
    unittest.main()
