"""

Write a Python program to find the maximum and minimum values in a given list within a specified index range.

[4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]

Index range:
3 to 8

(5, 0)

"""


def main():
    lst = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
    print(max(lst[3:9]), min(lst[3:9]))


if __name__ == "__main__":
    main()
