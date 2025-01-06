"""

Write a Python program to sum a specific column of a list in a given list of lists.

[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

1st: 12
2nd: 15
4th: 9

"""


def main():
    lst = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

    for c in (1, 2, 4):
        print(sum([lst[i][c-1] for i in range(len(lst))]))


if __name__ == "__main__":
    main()
