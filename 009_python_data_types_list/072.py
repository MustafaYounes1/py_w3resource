"""

Write a Python program to flatten a given nested list structure.

[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

"""

from itertools import chain


def main():
    lst = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
    res = []

    for _ in lst:
        if isinstance(_, list):
            res += _

        elif isinstance(_, int):
            res.append(_)

        else:
            raise TypeError("Expected only integers and lists")

    print(res)

if __name__ == "__main__":
    main()
