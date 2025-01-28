"""

Write a Python program to count the frequency of the elements of a given unordered list.

[2, 1, 3, 8, 5, 1, 4, 2, 3, 4, 0, 8, 2, 0, 8, 4, 2, 3, 4, 2]

{0: 2, 1: 2, 2: 5, 3: 3, 4: 4, 5: 1, 8: 3}

"""

from itertools import groupby


def main():
    lst = [2, 1, 3, 8, 5, 1, 4, 2, 3, 4, 0, 8, 2, 0, 8, 4, 2, 3, 4, 2]
    print({k: len(list(g)) for k, g in groupby(sorted(lst))})


if __name__ == "__main__":
    main()
