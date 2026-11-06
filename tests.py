import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(10), 314.1592654, places=7)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(10), 62.8318531, places=7)

    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_negtive(self):
        self.assertRaises(ValueError, circle_area, -10)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, circle_perimeter, -10)
    
    def test_area_string(self):
        self.assertRaises(TypeError, circle_area, "10")

    def test_perimeter_string(self):
        self.assertRaises(TypeError, circle_perimeter, "10")


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(5, 10), 25)

    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(1, 2, 3), 6)

    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 0), 0)

    def test_area_negtive(self):
        self.assertRaises(ValueError, triangle_area, -5, -10)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, triangle_perimeter, -1, -2, -3)
    
    def test_area_string(self):
        self.assertRaises(TypeError, triangle_area, "5", "10")

    def test_perimeter_string(self):
        self.assertRaises(TypeError, triangle_perimeter, "1", "2", "3")


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(5), 25)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_area_negtive(self):
        self.assertRaises(ValueError, square_area, -5)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, square_perimeter, -5)
    
    def test_area_string(self):
        self.assertRaises(TypeError, square_area, "5")

    def test_perimeter_string(self):
        self.assertRaises(TypeError, square_perimeter, "5")


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(10, 15), 150)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(10, 15), 50)

    def test_area_zero(self):
        self.assertEqual(rectangle_area(100, 0), 0)

    def test_area_negtive(self):
        self.assertRaises(ValueError, rectangle_area, -10, -15)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, rectangle_perimeter, -10, -15)
    
    def test_area_string(self):
        self.assertRaises(TypeError, rectangle_area, "10", "15")

    def test_perimeter_string(self):
        self.assertRaises(TypeError, rectangle_perimeter, "10", "15")
