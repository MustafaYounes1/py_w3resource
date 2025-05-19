"""

Write a Python program that creates a function that determines if a given point (x, y) is within a specified circle
area using boolean conditions.

Circle(cx: 10, cy: 10, r: 50),  Point(2, 3)      =>  True
Circle(cx: 5, cy: 4, r: 4),     Point(8, 9)      =>  False

"""

from dataclasses import dataclass
from math import sqrt


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Circle:
    center: Point
    radius: int


def is_point_inside_circle(c: Circle, pt: Point) -> bool:
    return sqrt((c.center.x - pt.x) ** 2 + (c.center.y - pt.y) ** 2) <= c.radius


def main():
    data = [
        [Circle(Point(10, 10), 50), Point(2, 3)],
        [Circle(Point(5, 4), 4), Point(8, 9)],
    ]

    for c, pt in data:
        print(is_point_inside_circle(c, pt))


if __name__ == "__main__":
    main()
