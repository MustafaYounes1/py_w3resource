"""

Write a Python program to create a generator function that generates all factors of a given number.

1000    =>  [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000]
56      =>  [1, 2, 4, 7, 8, 14, 28, 56]
97      =>  [1, 97]

"""

from typing import Generator


def factors_gen(n: int) -> Generator[int, None, None]:
    for _ in range(1, n + 1):
        if n % _ == 0:
            yield _


def main():
    data = [1000, 56, 97]

    for _ in data:
        print(list(factors_gen(_)))


if __name__ == "__main__":
    main()
