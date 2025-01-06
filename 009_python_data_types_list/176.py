"""

Write a Python program to create a new list by dividing two given lists of numbers.

[7, 2, 3, 4, 9, 2, 3]
[9, 8, 2, 3, 3, 1, 2]

[0.7777777777777778, 0.25, 1.5, 1.3333333333333333, 3.0, 2.0, 1.5]

"""


def main():
    lst1 = [7, 2, 3, 4, 9, 2, 3]
    lst2 = [9, 8, 2, 3, 3, 1, 2]

    print([a / b for a, b in zip(lst1, lst2)])


if __name__ == "__main__":
    main()
