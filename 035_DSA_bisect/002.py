"""

Write a Python program to locate the right insertion point for a specified value in sorted order.

[1, 2, 4, 7], 6         =>  3
[1, 2, 3, 4, 7], 3      =>  3

"""

from bisect import bisect_right


def main():
    data = [
        [[1, 2, 4, 7], 6],
        [[1, 2, 3, 4, 7], 3]
    ]

    for lst, item in data:
        print(bisect_right(lst, item))


if __name__ == "__main__":
    main()
