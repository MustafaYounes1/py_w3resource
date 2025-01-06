"""

Write a Python program to create a list of empty dictionaries.

[{}, {}, {}, {}, {}]

"""


def main():
    print([{} for _ in range(5)])


if __name__ == "__main__":
    main()
