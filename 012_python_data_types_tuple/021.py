"""

Write a Python program to replace the last value of tuples with '100' in a list.

[(10, 20, 40), (40, 50, 60), (70, 80, 90)]

[(10, 20, 100), (40, 50, 100), (70, 80, 100)]

"""


def main():
    lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    print([_[:-1] + (100, ) for _ in lst])


if __name__ == "__main__":
    main()
