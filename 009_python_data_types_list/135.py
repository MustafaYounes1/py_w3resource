"""

Write a Python program to iterate over all pairs of consecutive items in a given list.

[1, 1, 2, 3, 3, 4, 4, 5]

[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]

"""


def main():
    lst = [1, 1, 2, 3, 3, 4, 4, 5]
    print([(a, b) for a, b in zip(lst[:-1], lst[1::1])])


if __name__ == "__main__":
    main()
