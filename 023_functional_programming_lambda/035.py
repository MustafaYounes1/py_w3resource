"""

Write a Python program to check whether a specified list is sorted or not using lambda.

[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]                                 =>  True
[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]        =>  False

"""

from typing import Callable


def main():
    data = [
        [1, 2, 4, 6, 8, 10, 12, 14, 16, 17],
        [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
    ]

    f: Callable[[list[int]], bool] = lambda _: all(b >= a for a, b in zip(_[:-1], _[1:]))

    for _ in data:
        print(f(_))


if __name__ == "__main__":
    main()
