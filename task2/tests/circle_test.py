import unittest
from ..area_calculator.shapes import Circle
from math import pi


class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(Circle(3).get_area(), pi * 3 ** 2)
        self.assertEqual(Circle(2.5).get_area(), pi * 2.5 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, Circle, -1)

    def test_types(self):
        self.assertRaises(TypeError, Circle, "circle")
        self.assertRaises(TypeError, Circle, 1 + 2j)
        self.assertRaises(TypeError, Circle, True)
        self.assertRaises(TypeError, Circle, [1, 2])


if __name__ == '__main__':
    unittest.main()
