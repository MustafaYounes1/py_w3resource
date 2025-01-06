"""

Write a Python program to generate groups of five consecutive numbers in a list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(
        [lst[i: i+5] for i in range(0, len(lst), 5)]
    )


if __name__ == "__main__":
    main()
