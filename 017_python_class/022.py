"""

Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a
rectangle.

length = 12, width = 10     =>  area = 120

"""


class Rectangle:
    def __init__(self, length: float, width: float):
        self.__l: float = length
        self.__w: float = width

    @property
    def area(self) -> float:
        return self.__l * self.__w


def main():
    r = Rectangle(12, 10)
    print(r.area)


if __name__ == "__main__":
    main()
