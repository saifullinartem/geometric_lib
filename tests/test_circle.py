
import unittest
from geometric_lib.circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(3), 28.26)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2.5), 19.625)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 18.84)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(2.5), 15.7)

if __name__ == '__main__':
    unittest.main()
