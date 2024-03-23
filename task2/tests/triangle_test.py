import unittest
from ..area_calculator.shapes import Triangle
from math import sqrt


class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Triangle(2, 2, 2).get_area(), sqrt(3))

    def test_right_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_triangle())
        self.assertFalse(Triangle(1, 1, 1).is_right_triangle())

    def test_value(self):
        self.assertRaises(ValueError, Triangle, 1, 1, 0)
        self.assertRaises(ValueError, Triangle, 1, 0, 1)
        self.assertRaises(ValueError, Triangle, 0, 1, 1)


    def test_types(self):
        self.assertRaises(TypeError, Triangle, 1, 1, "1")
        self.assertRaises(TypeError, Triangle, 1, 2 + 3j, 1)
        self.assertRaises(TypeError, Triangle, False, 1, 1)
        self.assertRaises(TypeError, Triangle, 1, 1, [3])

    def test_triangle_existence(self):
        self.assertRaises(ValueError, Triangle, 1, 1, 2)
        self.assertRaises(ValueError, Triangle, 1, 2, 1)
        self.assertRaises(ValueError, Triangle, 2, 1, 1)


if __name__ == '__main__':
    unittest.main()
