"""

Write a Python program to pair consecutive elements of a given list.

[1, 2, 3, 4, 5, 6]
[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

[1, 2, 3, 4, 5]
[[1, 2], [2, 3], [3, 4], [4, 5]]

"""


def main():
    data = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5]
    ]

    for lst in data:
        print(list(zip(lst[:-1], lst[1:])))


if __name__ == "__main__":
    main()
