"""

Write a Python program to get the class name of an instance in Python.

Create a dummy class called Dummy that has the following private attributes: (d1 and d2) and a method called do_nothing
Instantiate te dummy class

The class name of the created instance:  Dummy

"""


class Dummy:
    def __init__(self, d1: float = 0., d2: float = 0.):
        self.__d1 = d1
        self.__d2 = d2

    def do_nothing(self) -> None:
        pass


def main():
    d = Dummy()
    print(type(d).__name__)


if __name__ == "__main__":
    main()
