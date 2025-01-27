"""

Write a Python program to count float values in a mixed list using lambda.

[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]   =>  3

"""


def main():
    lst = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
    print(len(list(filter(lambda _: isinstance(_, float), lst))))


if __name__ == "__main__":
    main()
