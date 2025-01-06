"""

Write a Python program to sort a given list of lists by length and value.

[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

"""


def main():
    lst = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
    print(sorted(lst, key=lambda _: (len(_), *_)))


if __name__ == "__main__":
    main()
