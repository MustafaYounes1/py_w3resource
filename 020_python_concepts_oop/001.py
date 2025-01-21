"""

Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

Circle(radius=5.7)

Area:       102.07
Perimeter:   35.81

"""

import math


class Circle:
    def __init__(self, radius: float):
        self.__r: float = radius

    @property
    def area(self) -> float:
        return math.pi * pow(self.__r, 2)

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.__r


def main():
    c = Circle(5.7)
    print(f"Area:       {c.area:6.2f}")
    print(f"Perimeter:  {c.perimeter:6.2f}")


if __name__ == "__main__":
    main()
