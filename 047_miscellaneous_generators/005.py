"""

Write a Python program to implement a generator function that generates all permutations of a given list of elements.

[1, 2]      =>  [(1, 2), (2, 1)]
[1, 2, 3]   =>  [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

"""

from itertools import permutations
from typing import Generator


def permute_gen(lst: list[int]) -> Generator[tuple[int, ...], None, None]:
    yield from permutations(lst, r=len(lst))


def main():
    data = [
        [1, 2],
        [1, 2, 3]
    ]

    for _ in data:
        print(list(permute_gen(_)))


if __name__ == "__main__":
    main()
