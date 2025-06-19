"""

Write a Python program to implement a generator that yields all possible combinations of a given list of elements.

[1, 2, 3, 4], 3     =>  [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
[1, 2, 3, 4], 4     =>  [(1, 2, 3, 4)]

"""

from itertools import combinations
from typing import Generator


def comb_gen(lst: list[int], r: int) -> Generator[tuple[int, ...], None, None]:
    yield from combinations(lst, r)


def main():
    data = [
        [[1, 2, 3, 4], 3],
        [[1, 2, 3, 4], 4],
    ]

    for lst, l in data:
        print(list(comb_gen(lst, l)))


if __name__ == "__main__":
    main()
