"""

Write a Python program that multiplies each number in a list with a given number using lambda functions.

2, [2, 4, 6, 9, 11] =>  4 8 12 18 22

"""

from typing import Callable


def main():
    f: Callable[[int | float, list[int | float]], list[int | float]] = lambda n, lst: list(map(lambda _: _ * n, lst))
    print(f(2, [2, 4, 6, 9, 11]))


if __name__ == "__main__":
    main()
