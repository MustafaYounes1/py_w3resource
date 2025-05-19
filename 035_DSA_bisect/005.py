"""

Write a Python program to find the index position of the largest value smaller than a given number in a sorted list
using Binary Search (bisect).

[1, 2, 3, 4, 8, 8, 10, 12], 5]      =>  4
[1, 2, 3, 4, 8, 8, 10, 12], 13]     =>  12
[1, 2, 3, 4, 8, 8, 10, 12], 0]      =>  None
[1, 2, 3, 4, 8, 8, 10, 12], -12]    =>  None

"""

from bisect import bisect_left


def largest_smaller_value(lst: list[...], item: ...) -> ...:
    pos = bisect_left(lst, item) - 1

    if pos < len(lst) and lst[pos] < item:
        return lst[pos]
    else:
        return None


def main():
    data = [
        [[1, 2, 3, 4, 8, 8, 10, 12], 5],
        [[1, 2, 3, 4, 8, 8, 10, 12], 13],
        [[1, 2, 3, 4, 8, 8, 10, 12], 0],
        [[1, 2, 3, 4, 8, 8, 10, 12], -12],
    ]

    for lst, item in data:
        print(largest_smaller_value(lst, item))


if __name__ == "__main__":
    main()
