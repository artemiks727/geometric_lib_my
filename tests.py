import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(circle_area(10), math.pi * 100, places=7)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle_perimeter(10), 2 * math.pi * 10, places=7)

    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)


class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(triangle_area(5, 10), 25)

    def test_perimeter_positive(self):
        self.assertEqual(triangle_perimeter(1, 2, 3), 6)

    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 0), 0)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(5), 25)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)


class RectangleTestCase(unittest.TestCase):
    def test_area_square_mul(self):
        self.assertEqual(rectangle_area(10, 10), 100)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(10, 10), 40)

    def test_area_zero(self):
        self.assertEqual(rectangle_area(100, 0), 0)
