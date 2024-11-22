
import unittest
from geometric_lib.triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 2), 5.0)
        self.assertEqual(area(0, 0), 0.0)
        self.assertEqual(area(3.5, 4), 7.0)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(2.5, 3.5, 4.5), 10.5)

if __name__ == '__main__':
    unittest.main()
