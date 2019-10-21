import unittest

class TestPoint2D(unittest.TestCase):
    def test_clockwise(self):
        a = Point2D(1, 5)
        b = Point2D(3, 4)
        c = Point2D(-3, 6)
        self.assertEqual(Point2D().ccw(a, b, c),-1)

    def test_anticlockwise(self):
        a = Point2D(1, 5)
        b = Point2D(-6, 8)
        c = Point2D(-3, 6)
        self.assertEqual(Point2D().ccw(a, b, c), 1)

    def test_collinear(self):
        a = Point2D(1, 0)
        b = Point2D(3, 0)
        c = Point2D(-3, 0)
        self.assertEqual(Point2D().ccw(a, b, c), 0)

class Point2D(object):
    x = 0
    y = 0

    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def ccw(self, a, b, c):
        area2 = (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
        if area2 < 0:
            return -1
        elif area2 > 0:
            return 1
        else:
            return 0

if __name__ == "__main__":
    unittest.main()