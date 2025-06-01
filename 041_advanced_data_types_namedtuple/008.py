"""

Write a Python program that defines a NamedTuple named "Triangle" with fields 'side_1', 'side_2', and 'side_3'.
Now write a function that takes a "Triangle" NamedTuple as input and calculates its area using Heron's formula.

The area of a triangle can be calculated using Heron's formula, which utilizes the semi-perimeter. The semi-perimeter
(s) is half the perimeter of the triangle, and the formula is: Area = √(s(s-a)(s-b)(s-c)), where a, b, and c are the
side lengths of the triangle.

Triangle(side_1=4, side_2=5, side_3=7)  ->  9.797958971132712

"""

import math
from typing import NamedTuple


class Triangle(NamedTuple):
    side_1: float
    side_2: float
    side_3: float


def triangle_area(t: Triangle) -> float:
    s = sum((t.side_1, t.side_2, t.side_3)) / 2
    return math.sqrt(s * (s - t.side_1) * (s - t.side_2) * (s - t.side_3))


def main():
    t = Triangle(4, 5, 7)
    print(triangle_area(t))


if __name__ == "__main__":
    main()
