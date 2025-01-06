"""

Write a Python program to calculate the difference between the two lists.

[1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]  => [9, 3, 5, 8, 2, 4, 6]

"""


def main():
    lst1, lst2 = [1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]
    print(list(set(lst1).symmetric_difference(set(lst2))))


if __name__ == "__main__":
    main()
