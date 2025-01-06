"""

Write a Python program to get items from a given list that are even and greater than 45.

[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

[78, 90, 100, 76, 62]

"""


def main():
    lst = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
    print(list(filter(lambda _: _ % 2 == 0 and _ > 45, lst)))


if __name__ == "__main__":
    main()
