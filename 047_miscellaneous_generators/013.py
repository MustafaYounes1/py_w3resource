"""

Write a Python program to create a generator that generates the square, cube roots of numbers from 1 to n.

n= 1, ( 1)^2 = 1.00, ( 1)^3 = 1.00
n= 2, ( 2)^2 = 1.41, ( 2)^3 = 1.26
n= 3, ( 3)^2 = 1.73, ( 3)^3 = 1.44
n= 4, ( 4)^2 = 2.00, ( 4)^3 = 1.59
n= 5, ( 5)^2 = 2.24, ( 5)^3 = 1.71
n= 6, ( 6)^2 = 2.45, ( 6)^3 = 1.82
n= 7, ( 7)^2 = 2.65, ( 7)^3 = 1.91
n= 8, ( 8)^2 = 2.83, ( 8)^3 = 2.00
n= 9, ( 9)^2 = 3.00, ( 9)^3 = 2.08
n=10, (10)^2 = 3.16, (10)^3 = 2.15

"""

from dataclasses import dataclass
from math import cbrt, sqrt
from typing import Generator


@dataclass
class Root:
    n: int
    square_r: float
    cube_r: float

    def __repr__(self):
        return f"n={self.n:2d}, ({self.n:2d})^2 = {self.square_r:4.2f}, ({self.n:2d})^3 = {self.cube_r:4.2f}"


def roots_gen(n: int) -> Generator[Root, None, None]:
    for i in range(1, n + 1):
        yield Root(i, sqrt(i), cbrt(i))


def main():
    print("\n".join(map(str, list(roots_gen(10)))))


if __name__ == "__main__":
    main()
