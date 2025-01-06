"""

Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.

[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], [13, 17]
[[13, 14, 15, 17]]

"""


def main():
    lst, r = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], range(13, 18)
    print(list(filter(lambda _: all(__ in r for __ in _), lst)))


if __name__ == "__main__":
    main()
