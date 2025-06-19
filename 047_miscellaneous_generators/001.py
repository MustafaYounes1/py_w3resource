"""

Write a Python program that creates a generator function that yields cubes of numbers from 1 to n.
Accept n from the user.

"""

from typing import Generator


def cubes(n: int) -> Generator[int, None, None]:
    i = 1

    while i <= n:
        yield i ** 3
        i += 1


def main():
    n = int(input("Enter n: "))
    gen = cubes(n)

    for _ in gen:
        print(_)


if __name__ == "__main__":
    main()
