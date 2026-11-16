from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return ("Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", "
                + str(self.pt2.x) + ", " + str(self.pt2.y) + ")")

    def __eq__(self, other):        # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta (Point)
        x_c = (self.pt1.x + self.pt2.x) / 2
        y_c = (self.pt1.y + self.pt2.y) / 2
        return Point(x_c, y_c)

    def area(self):                 # pole powierzchni (liczba)
        a = self.pt2.x - self.pt1.x
        b = self.pt2.y - self.pt1.y
        return a * b

    def move(self, x, y):           # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

import unittest

class TestRectangle(unittest.TestCase):
    def test_init(self):
        pass
    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 5, 7)), "[(1,2), (5,7)]")
        self.assertEqual(str(Rectangle(2, 1, 7, 5)), "[(2,1), (7,5)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 2, 5, 7)), "Rectangle(1, 2, 5, 7)")
        self.assertEqual(repr(Rectangle(2, 1, 7, 5)), "Rectangle(2, 1, 7, 5)")

    def test_eq(self):
        r1 = Rectangle(1, 2, 5, 7)
        r2 = Rectangle(1, 2, 5, 7)
        r3 = Rectangle(0, 0, 3, 4)
        self.assertEqual(r1, r2)
        self.assertNotEqual(r1, r3)

    def test_ne(self):
        r1 = Rectangle(1, 2, 5, 7)
        r2 = Rectangle(1, 2, 5, 7)
        r3 = Rectangle(0, 0, 3, 4)
        self.assertNotEqual(r1, r3)
        self.assertFalse(r1 != r2)

    def test_center(self):
        r = Rectangle(1, 2, 5, 8)
        self.assertEqual(r.center(), Point(3.0, 5.0))

    def test_area(self):
        r = Rectangle(1, 2, 5, 7)
        self.assertEqual(r.area(), 20)

    def test_move(self):
        r = Rectangle(1, 2, 5, 7)
        r.move(2, 3)
        self.assertEqual(r.pt1, Point(3, 5))
        self.assertEqual(r.pt2, Point(7, 10))

if __name__ == '__main__':
    unittest.main()