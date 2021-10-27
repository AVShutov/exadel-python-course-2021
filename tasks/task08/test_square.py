import unittest
from shapes import Point2D, Square


class TestShapes(unittest.TestCase):
    square = Square(Point2D(5, 10), 20)

    def test_square_area(self):
        self.assertEqual(self.square.area(), 400)

    def test_square_contains_Point2D(self):
        self.assertTrue(Point2D(6, 9) in self.square)

    def test_square_not_contains_Point2D(self):
        self.assertFalse(Point2D(0, -3) in self.square)


if __name__ == '__main__':
    unittest.main()