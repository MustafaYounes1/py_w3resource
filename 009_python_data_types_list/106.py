"""

Write a Python program to count integers in a given mixed list.

[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]  =>  6

"""


def main():
    lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
    print(len(list(filter(lambda _: isinstance(_, int), lst))))


if __name__ == "__main__":
    main()
