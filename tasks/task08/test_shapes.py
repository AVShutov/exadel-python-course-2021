import unittest
from shapes import *

rectangle = Rectangle(Point2D(10, 15), 10, 20)
square = Square(Point2D(5, 10), 20)
circle = Circle(Point2D(30, 40), 35)


class TestShapes(unittest.TestCase):

    def test_rectangle(self):
        self.assertEqual(rectangle.area(), 200)
        self.assertEqual(Point2D(12, 14) in rectangle, True)
        self.assertEqual(Point2D(11, 3) in rectangle, False)


    def test_square(self):
        self.assertEqual(square.area(), 400)
        self.assertEqual(Point2D(6, 9) in square, True)
        self.assertEqual(Point2D(15, 20) in square, False)

    def test_circle(self):
        self.assertEqual(circle.area(), 3848.4510006474966)
        self.assertEqual(Point2D(31, 39) in circle, True)
        self.assertEqual(Point2D(100, 200) in circle, False)


if __name__ == '__main__':
    unittest.main()