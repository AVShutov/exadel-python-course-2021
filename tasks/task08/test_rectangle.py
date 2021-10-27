import unittest
from shapes import Point2D, Rectangle


class TestRectangle(unittest.TestCase):
    rectangle = Rectangle(Point2D(10, 15), 10, 20)

    def test_rectangle_area(self):
        self.assertEqual(self.rectangle.area(), 200)

    def test_rectangle_contains_Point2D(self):
        self.assertTrue(Point2D(12, 14) in self.rectangle)

    def test_rectangle_not_contains_Point2D(self):
        self.assertFalse(Point2D(-12, 0) in self.rectangle)

if __name__ == '__main__':
    unittest.main()