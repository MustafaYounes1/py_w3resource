"""

Write a Python function that checks if a given list is sorted in descending order. Return None if the list is empty.

[7, 7, 8, 2, 1]     =>  False
[1, 2, 3, 4, 5]     =>  False
[5, 4, 3, 2, 1]     =>  True
[]                  =>  None

"""

from itertools import pairwise


def validate_descending_order(lst: list[...]) -> bool | None:
    if not lst:
        return None

    for a, b in pairwise(lst):
        if a < b:
            return False

    return True


def main():
    data = [
        [7, 7, 8, 2, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [],
    ]

    for _ in data:
        print(validate_descending_order(_))


if __name__ == "__main__":
    main()
