"""

Write a Python program to generate combinations of n distinct objects taken from the elements of a given list.

[1, 2, 3, 4, 5, 6, 7, 8, 9], 2

(1, 2) (1, 3) (1, 4) (1, 5) (1, 6) (1, 7) (1, 8) (1, 9) (2, 3) (2, 4) (2, 5) (2, 6) (2, 7) (2, 8) (2, 9) (3, 4) (3,
5) (3, 6) (3, 7) (3, 8) (3, 9) (4, 5) (4, 6) (4, 7) (4, 8) (4, 9) (5, 6) (5, 7) (5, 8) (5, 9) (6, 7) (6, 8) (6,
9) (7, 8) (7, 9) (8, 9)

"""

from itertools import combinations


def main():
    lst, r = [1, 2, 3, 4, 5, 6, 7, 8, 9], 2
    print(list(combinations(lst, r)))


if __name__ == "__main__":
    main()
