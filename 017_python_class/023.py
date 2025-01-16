"""

Write a Python class named Circle constructed from a radius and two methods that will compute the area and the
perimeter of a circle.

Radius is 8

Area:      201.06192982974676
Perimeter: 50.26548245743669

"""

from math import pi


class Circle:
    def __init__(self, r: float):
        self.__r: float = r

    @property
    def area(self) -> float:
        return pi * pow(self.__r, 2)

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.__r


def main():
    c = Circle(8)
    print(f"Area:      {c.area}")
    print(f"Perimeter: {c.perimeter}")


if __name__ == "__main__":
    main()
