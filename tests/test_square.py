
import unittest
from geometric_lib.square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(2.5), 6.25)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(2.5), 10)

if __name__ == '__main__':
    unittest.main()
