"""

Write a Python program to create a function that takes one argument, and that argument will be multiplied with
an unknown given number.

Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75

"""

from typing import Callable


def f(a: int | float) -> Callable[[int | float], int | float]:
    return lambda b: a * b


def main():
    closure = f(15)
    print(closure(2))
    print(closure(3))
    print(closure(4))
    print(closure(5))


if __name__ == "__main__":
    main()
