"""

Replace all even numbers in a list with their negative.

e.g.    [1, 2, 3, 4, 5, 6, 7, 8, 9]     =>      [1, -2, 3, -4, 5, -6, 7, -8, 9]
"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print([_ * -1 if _ % 2 == 0 else _ for _ in lst])


if __name__ == "__main__":
    main()
