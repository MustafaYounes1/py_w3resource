"""

Write a Python program to create a generator function that generates the powers of a number up to a specified exponent.

2, 3    =>  [1, 2, 4, 8]
8, 4    =>  [1, 8, 64, 512, 4096]

"""

from typing import Generator


def powers_gen(n: int, max_exp: int) -> Generator[int, None, None]:
    res = 1

    for i in range(max_exp + 1):
        yield res
        res *= n


def main():
    data = [
        (2, 3),
        (8, 4)
    ]

    for base, max_exp in data:
        print(list(powers_gen(base, max_exp)))


if __name__ == "__main__":
    main()
