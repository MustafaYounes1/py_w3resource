"""

Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a
list of the numbers.

n = 10
[0, 1, 1, 4, 9, 25, 64, 169, 441, 1156]

"""

from typing import Callable


def main():
    f: Callable[[int], list[int]] = lambda x: 0 if x == 0 else 1 if x == 1 else f(x - 1) + f(x - 2)
    print(list(map(lambda _: pow(f(_), 2), range(0, 10))))


if __name__ == "__main__":
    main()
