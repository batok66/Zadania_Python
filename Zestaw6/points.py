import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):              # zwraca string "(x, y)"
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __repr__(self):             # zwraca string "Point(x, y)"
        return "Point(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):        # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):       # v1 + v2
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):       # v1 - v2
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):               # długość wektora
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def test_init(self): pass

    def test_str(self):
        self.assertEqual(str(Point(1, 2)), "(1,2)")
        self.assertEqual(str(Point(0, 5)), "(0,5)")

    def test_repr(self):
        self.assertEqual(repr(Point(1, 2)), "Point(1,2)")
        self.assertEqual(repr(Point(0, 5)), "Point(0,5)")

    def test_eq(self):
        self.assertTrue((Point(1, 2) == Point(1, 2)))
        self.assertFalse((Point(1, 5) == Point(0, 5)))

    def test_ne(self):
        self.assertTrue((Point(1, 2) != Point(2, 2)))
        self.assertFalse((Point(0, 5) != Point(0, 5)))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(2, 3), Point(3, 5))
        self.assertEqual(Point(2, 2) + Point(0, 3), Point(2, 5))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(2, 3), Point(-1, -1))
        self.assertEqual(Point(2, 2) - Point(0, 3), Point(2, -1))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(2, 3), 8)
        self.assertEqual(Point(2, 2) * Point(0, 3), 6)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(2, 3)), -1)
        self.assertEqual(Point(2, 3).cross(Point(1, 2)), 1)

    def test_length(self):
        self.assertEqual(Point(1, 2).length(), math.sqrt(5))
        self.assertEqual(Point(3, 4).length(), 5)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash(Point(1, 2)))
        self.assertNotEqual(hash(Point(0, 3)), hash(Point(0, 2)))

if __name__ == '__main__':
    unittest.main()