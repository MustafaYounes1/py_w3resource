"""

Replace all odd numbers in a list with -1.

e.g.    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     =>  [-1, 2, -1, 4, -1, 6, -1, 8, -1, 10]
"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print([_ if _ % 2 == 0 else -1 for _ in lst])


if __name__ == "__main__":
    main()
