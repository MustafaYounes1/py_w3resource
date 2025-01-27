"""

Write a Python program to find the intersection of two given lists using Lambda.

[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]

[8, 1, 2, 9]

"""

from typing import Callable


def main():
    f: Callable[[list[...], list[...]], list[...]] = lambda l1, l2: list(set(l1) & set(l2))
    print(f([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]))

if __name__ == "__main__":
    main()
