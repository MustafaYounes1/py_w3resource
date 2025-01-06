"""

Write a Python program to find the list in a list of lists whose sum of elements is the highest.

[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

[10, 11, 12]

"""


def main():
    lst = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
    print(max(lst, key=lambda _: sum(_)))


if __name__ == "__main__":
    main()
