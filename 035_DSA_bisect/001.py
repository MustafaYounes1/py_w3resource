"""

Write a Python program to locate the left insertion point for a specified value in sorted order.

[1, 2, 4, 5], 6     =>  4
[1, 2, 4, 5], 3     =>  2

"""

from bisect import bisect_left


def main():
    data = [
        [[1, 2, 4, 5], 6],
        [[1, 2, 4, 5], 3]
    ]

    for lst, item in data:
        print(bisect_left(lst, item))


if __name__ == "__main__":
    main()
