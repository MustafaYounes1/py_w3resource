"""

Write a Python program to find the maximum and minimum values of the three given lists.

[2, 3, 5, 8, 7, 2, 3]
[4, 3, 9, 0, 4, 3, 9]
[2, 1, 5, 6, 5, 5, 4]

max:    9
min:    0

"""

from itertools import chain


def main():
    data = [
        [2, 3, 5, 8, 7, 2, 3],
        [4, 3, 9, 0, 4, 3, 9],
        [2, 1, 5, 6, 5, 5, 4]
    ]

    data = list(chain.from_iterable(data))
    print(max(data))
    print(min(data))

if __name__ == "__main__":
    main()
