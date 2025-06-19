"""

Write a Python program to implement a generator that generates random numbers within a given range.

"""

import random
from typing import Generator


def random_number(a: int, b: int) -> Generator[int, None, None]:
    """Infinite random number generator"""
    while True:
        yield random.randint(a, b)


def main():
    gen = random_number(10, 100)
    print(next(gen))
    print(next(gen))


if __name__ == "__main__":
    main()
