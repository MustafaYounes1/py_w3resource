"""

Write a Python program to find the indexes of all None items in a given list.

[1, None, 5, 4, None, 0, None, None]
[1, 4, 6, 7]

"""


def main():
    lst = [1, None, 5, 4, None, 0, None, None]
    print([idx for idx, _ in enumerate(lst) if _ is None])


if __name__ == "__main__":
    main()
