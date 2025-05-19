"""

Write a Python program to find the first/last occurrence of a given number in a sorted list using Binary Search (bisect).
Note: return -1 if the element doesn't exist in the list

[1, 2, 3, 4, 8, 8, 10, 12], 8]      =>  4, 5
[1, 2, 3, 4, 8, 8, 10, 12], 80]     =>  -1, -1
[1, 2, 3, 4, 8, 8, 10, 12], -11]    =>  -1, -1
[1, 2, 3, 4, 8, 8, 10, 12], 12]     =>  7, 7

"""

from bisect import bisect_left, bisect_right


def first_occurrence(lst: list[...], item: ...) -> int:
    res = bisect_left(lst, item)

    if res < len(lst) and lst[res] == item:
        return res
    else:
        return -1


def last_occurrence(lst: list[...], item: ...) -> int:
    res = bisect_right(lst, item) - 1

    if 0 <= res < len(lst) and lst[res] == item:
        return res
    else:
        return -1


def main():
    data = [
        [[1, 2, 3, 4, 8, 8, 10, 12], 8],
        [[1, 2, 3, 4, 8, 8, 10, 12], 80],
        [[1, 2, 3, 4, 8, 8, 10, 12], -11],
        [[1, 2, 3, 4, 8, 8, 10, 12], 12],
    ]

    for lst, item in data:
        print(first_occurrence(lst, item), last_occurrence(lst, item))


if __name__ == "__main__":
    main()
