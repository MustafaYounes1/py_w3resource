"""

Write a Python program to get the symmetric difference between two iterables, without filtering out duplicate values.

[10, 20, 30], [10, 20, 40]  =>  [30, 40]

"""


def main():
    lst1, lst2 = [10, 20, 30], [10, 20, 40]
    inter = set(lst1).intersection(lst2)
    print([_ for _ in lst1 + lst2 if _ not in inter])


if __name__ == "__main__":
    main()
