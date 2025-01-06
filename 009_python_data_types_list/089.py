"""

Write a Python program to Zip two given lists of lists.

[[1, 3], [5, 7], [9, 11]]
[[2, 4], [6, 8], [10, 12, 14]]

[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
"""

from operator import add


def main():
    lst1 = [[1, 3], [5, 7], [9, 11]]
    lst2 = [[2, 4], [6, 8], [10, 12, 14]]

    print(list(map(add, lst1, lst2)))


if __name__ == "__main__":
    main()
