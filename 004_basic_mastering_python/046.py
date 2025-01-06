"""

Replace all even numbers in a list with the next odd number.

lst = [2, 5, 8, 12, 15]

[3, 5, 9, 13, 15]

"""


def main():
    lst = [2, 5, 8, 12, 15]
    print([i + 1 if i % 2 == 0 else i for i in lst])


if __name__ == "__main__":
    main()
