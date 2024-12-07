# tests/test_square.py

import unittest
from .square import area, perimeter

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

if __name__ == '__main__':
    unittest.main()
