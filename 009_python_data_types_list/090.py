"""

Write a Python program to count the number of lists in a given list of lists.

[[1, 3], [5, 7], [9, 11], [13, 15, 17]]         =>  4
[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]     =>  3

"""


def main():
    data = [
        [[1, 3], [5, 7], [9, 11], [13, 15, 17]],
        [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
    ]

    for _ in data:
        print(len(_))


if __name__ == "__main__":
    main()
