import unittest
from shapes import Point2D, Circle


class TestShapes(unittest.TestCase):
    circle = Circle(Point2D(30, 40), 35)

    def test_circle_area(self):
        self.assertEqual(self.circle.area(), 3848.4510006474966)

    def test_circle_contains_Point2D(self):
        self.assertTrue(Point2D(31, 39) in self.circle)

    def test_circle_not_contains_Point2D(self):
        self.assertFalse(Point2D(-100, 200) in self.circle)


if __name__ == '__main__':
    unittest.main()