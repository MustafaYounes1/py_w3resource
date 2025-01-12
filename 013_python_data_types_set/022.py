"""

Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
Note: try to use Python sets to eliminate duplicate pairs

[10, 11, 12, 13, 14, 15, 11, 16, 17, 18, 19, 20], 35

[(17, 18), (16, 19), (15, 20)]

"""

from itertools import combinations


def main():
    lst, c = [10, 11, 12, 13, 14, 15, 11, 16, 17, 18, 19, 20], 35
    print(
        [_ for _ in set(combinations(lst, 2)) if sum(_) == c]
    )


if __name__ == "__main__":
    main()
