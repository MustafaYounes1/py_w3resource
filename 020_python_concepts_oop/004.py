"""

Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
Implement subclasses for different shapes like circle, triangle, and rectangle.

Circle(radius=7)
Rectangle(Width=7, Length=5)
Triangle(sides=(4, 3, 5), base_idx=2, height=4)

==================================================
Circle(radius=7)
Area:       153.94
Perimeter:   43.98
==================================================
Rectangle(width=7, length=5)
Area:        35.00
Perimeter:   24.00
==================================================
Triangle(sides=(4, 3, 5), base=5, height=4)
Area:        10.00
Perimeter:   12.00
==================================================

"""

from abc import ABC, abstractmethod
import math
from typing import Tuple, Union


class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> Union[int, float]:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> Union[int, float]:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class Rectangle(Shape):
    def __init__(self, width: Union[int, float], length: Union[int, float]):
        self.__w: Union[int, float] = width
        self.__l: Union[int, float] = length

    @property
    def area(self) -> Union[int, float]:
        return self.__w * self.__l

    @property
    def perimeter(self) -> Union[int, float]:
        return 2 * (self.__w + self.__l)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(width={self.__w}, length={self.__l})"


class Triangle(Shape):
    def __init__(self, sides: Tuple[Union[int, float], ...], base_idx: int, height: Union[int, float]):
        assert base_idx in range(len(sides))
        self.__s: Tuple[Union[int, float], ...] = sides
        self.__b: Union[int, float] = sides[base_idx]
        self.__h: Union[int, float] = height

    @property
    def area(self) -> Union[int, float]:
        return 0.5 * self.__b * self.__h

    @property
    def perimeter(self) -> Union[int, float]:
        return sum(self.__s)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(sides={self.__s}, base={self.__b}, height={self.__h})"


class Circle(Shape):
    def __init__(self, radius: Union[int, float]):
        self.__r: Union[int, float] = radius

    @property
    def area(self) -> Union[int, float]:
        return math.pi * pow(self.__r, 2)

    @property
    def perimeter(self) -> Union[int, float]:
        return 2 * math.pi * self.__r

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(radius={self.__r})"


def main():
    s1 = Circle(radius=7)
    s2 = Rectangle(width=7, length=5)
    s3 = Triangle(sides=(4, 3, 5), base_idx=2, height=4)

    print("=" * 50)
    for s in (s1, s2, s3):
        print(s)
        print(f"Area:       {s.area:6.2f}")
        print(f"Perimeter:  {s.perimeter:6.2f}")
        print("=" * 50)


if __name__ == "__main__":
    main()
