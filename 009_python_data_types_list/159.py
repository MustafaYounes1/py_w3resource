"""

Write a Python program to append the same value/a list multiple times to a list/list-of-lists.

Add a value(7), 5 times, to a list:
['7', '7', '7', '7', '7']

Add 5, 6 times, to a list [1, 2, 3, 4]:
[1, 2, 3, 4, 5, 5, 5, 5, 5, 5]

Add a list [1, 2, 5], 4 times, to a list of lists:
[[1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]

Add a list [1, 2, 5], 3 times, to a list of lists [[5, 6, 7], [1, 2, 5]]:
[[5, 6, 7], [1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]

"""


def main():
    print(['7'] * 5)

    print([1, 2, 3, 4] + [5] * 6)

    print([[1, 2, 5] for _ in range(4)])

    print([[5, 6, 7], [1, 2, 5]] + [[1, 2, 5] for _ in range(3)])


if __name__ == "__main__":
    main()
