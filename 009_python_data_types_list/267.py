"""

Write a Python program to get the cumulative sum of the elements of a given list.

[1, 2, 3, 4]
[1, 3, 6, 10]

[-1, -2, -3, 4]
[-1, -3, -6, -2]

"""

from itertools import accumulate


def main():
    data = [
        [1, 2, 3, 4],
        [-1, -2, -3, 4]
    ]

    for lst in data:
        # the default function is operator.add
        print(list(accumulate(lst)))


if __name__ == "__main__":
    main()
