"""

Write a Python program to extract every nth element from a given two-dimensional list.

[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]

1st =>  [1, 4, 7]
3rd =>  [3, 6, 9]

"""


def main():
    lst = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
    for c in (1, 3):
        print([_[c-1] for _ in lst])


if __name__ == "__main__":
    main()
