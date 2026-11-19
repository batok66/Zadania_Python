from points import Point
import math

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):            # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):                # pole powierzchni
        return math.pi * self.radius * self.radius

    def move(self, x, y):          # przesuniecie o (x, y)
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):        # najmniejszy okrąg pokrywający oba
        d = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2) # odleglosc miedzy srodkami
        r_sum = self.radius + other.radius
        r_dif = abs(self.radius - other.radius)

        if d <= r_dif:
            if self.radius > other.radius: return Circle(self.pt.x, self.pt.y, self.radius)
            return Circle(other.pt.x, other.pt.y, other.radius)

        else:
            new_radius = (r_sum + d) / 2
            new_x = self.pt.x + (new_radius - self.radius) / d * (other.pt.x - self.pt.x)
            new_y = self.pt.y + (new_radius - self.radius) / d * (other.pt.y - self.pt.y)
            return Circle(new_x, new_y, new_radius)

import unittest

class TestCircle(unittest.TestCase):

    def test_init(self):
        c = Circle(1, 2, 3)
        self.assertEqual(c.pt, Point(1, 2))
        self.assertEqual(c.radius, 3)
        with self.assertRaises(ValueError):
            Circle(0, 0, -1)

    def test_repr(self):
        self.assertEqual(repr(Circle(1, 2, 3)), "Circle(1, 2, 3)")
        self.assertEqual(repr(Circle(0, 0, 0)), "Circle(0, 0, 0)")

    def test_eq(self):
        self.assertTrue(Circle(1, 2, 3) == Circle(1, 2, 3))
        self.assertFalse(Circle(1, 2, 3) == Circle(1, 2, 4))

    def test_ne(self):
        self.assertTrue(Circle(1, 2, 3) != Circle(0, 2, 3))
        self.assertFalse(Circle(1, 2, 3) != Circle(1, 2, 3))

    def test_area(self):
        self.assertAlmostEqual(Circle(0, 0, 1).area(), math.pi)
        self.assertAlmostEqual(Circle(5, 5, 2).area(), 4 * math.pi)

    def test_move(self):
        c = Circle(1, 2, 3)
        c.move(2, -5)
        self.assertEqual(c, Circle(3, -3, 3))
        c.move(0, 0)
        self.assertEqual(c, Circle(3, -3, 3))

    def test_cover(self):
        # okręgi przecinające się
        c = Circle(0, 0, 3).cover(Circle(6, 0, 5))
        self.assertAlmostEqual(c.pt.x, 4)
        self.assertAlmostEqual(c.pt.y, 0)
        self.assertAlmostEqual(c.radius, 7)
        # okręgi rozłączne
        c = Circle(0, 0, 1).cover(Circle(10, 0, 2))
        self.assertAlmostEqual(c.pt.x, 5.5)
        self.assertAlmostEqual(c.pt.y, 0)
        self.assertAlmostEqual(c.radius, 6.5)
        # okręgi wewnętrzne
        self.assertEqual(Circle(0, 0, 5).cover(Circle(1, 0, 2)), Circle(0, 0, 5))
        self.assertEqual(Circle(1, 0, 2).cover(Circle(0, 0, 5)), Circle(0, 0, 5))

