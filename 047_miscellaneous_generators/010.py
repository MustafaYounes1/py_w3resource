"""

Write a Python program that creates a generator function that generates all prime numbers between two given numbers.

1, 30       =>  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
100, 200    =>  [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
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
    for n in range(a, b + 1):
        if is_prime(n):
            yield n


def main():
    data = [
        (1, 30),
        (100, 200)
    ]

    for a, b in data:
        print(list(prime_gen(a, b)))


if __name__ == "__main__":
    main()
