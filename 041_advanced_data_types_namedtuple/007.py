"""

Write a Python program that defines a NamedTuple named "Circle" with fields 'radius' and 'center' (a Point NamedTuple
representing the coordinates of the center of the circle). Create an instance of the "Circle" NamedTuple and print its
attributes.

-> Circle(center=Point(x=0, y=0), radius=0.45)

"""

from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


class Circle(NamedTuple):
    center: Point
    radius: float


def main():
    c = Circle(Point(0, 0), 0.45)
    print(c)


if __name__ == "__main__":
    main()
