from typing import Union
from math import pi, sqrt

class Shape:
    def get_area(self):
        raise NotImplementedError("The get_area() method must be overridden in the child class")


class Circle(Shape):
    def __init__(self, radius: Union[int, float]) -> None:
        if type(radius)  not in [int, float]:
            raise TypeError("Radius must be only non-negative real number")
        if radius < 0:
            raise ValueError("Radius can't be negative")
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1: Union[int, float], side2: Union[int, float], side3: Union[int, float]) -> None:
        if type(side1) not in [int, float] or type(side2) not in [int, float] or type(side3) not in [int, float]:
            raise TypeError("All the sides must be only non-negative real numbers")
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All the sides must be positive numbers")
        if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
            raise ValueError("Triangle with given sides doesn't exist")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self) -> float:
        semiper = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(semiper * (semiper - self.side1) * (semiper - self.side2) * (semiper - self.side3))

    def is_right_triangle(self) -> bool:
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
