"""

Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument.
Also create a lambda function that multiplies argument x with argument y and prints the result.

f1(10)      =>  25
f2(12, 4)   =>  48

"""

from typing import Callable


def main():
    f1: Callable[[int | float], int | float] = lambda x: x + 15
    f2: Callable[[int | float, int], int | float] = lambda x, y: x * y

    print(f1(10))
    print(f2(12, 4))


if __name__ == "__main__":
    main()
