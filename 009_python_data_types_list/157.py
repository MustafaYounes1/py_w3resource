"""

Write a Python program to interleave lists of varying lengths.

[2, 4, 7, 0, 5, 8]
[2, 5, 8]
[0, 1]
[3, 3, -1, 7]

[2, 2, 0, 3, 4, 5, 1, 3, 7, 8, -1, 0, 7, 5, 8]

"""

from itertools import chain
import random


def main():
    random.seed(0)

    data = [
        [2, 4, 7, 0, 5, 8],
        [2, 5, 8],
        [0, 1],
        [3, 3, -1, 7]
    ]

    res = list(chain.from_iterable(data))
    random.shuffle(res)

    print(res)


if __name__ == "__main__":
    main()
