"""

Write a Python program that creates a generator function that generates all prime numbers between two given numbers.

0 - 100: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

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


def prime_gen(a: int, b: int) -> Generator[int, None, None]:
    for _ in range(a, b + 1):
        if is_prime(_):
            yield _


def main():
    gen = prime_gen(0, 100)
    print(list(gen))


if __name__ == "__main__":
    main()
