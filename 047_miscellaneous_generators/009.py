"""

Write a Python program that creates a generator that generates all prime factors of a given number.

1729        =>  [7, 13, 19]
8763        =>  [3, 23, 127]
36          =>  [2, 3]

"""

from math import sqrt
from typing import Generator


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def prime_factors(n: int) -> Generator[int, None, None]:
    for factor in range(2, n + 1):
        if n % factor == 0:
            if is_prime(factor):
                yield factor


def main():
    data = [1729, 8763, 36]

    for n in data:
        print(list(prime_factors(n)))


if __name__ == "__main__":
    main()
