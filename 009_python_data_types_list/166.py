"""

Write a Python program to remove the None value from a given list.

[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

[12, 0, 23, -55, 234, 89, 0, 6, -12]

"""


def main():
    lst = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
    print(list(filter(lambda _: _ is not None, lst)))


if __name__ == "__main__":
    main()
