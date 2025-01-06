"""

Write a Python program to check if the elements of a given list are unique or not.

[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]    =>  False
[2, 4, 6, 8, 10, 12, 14]                            =>  True

"""


def main():
    data = [
        [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17],
        [2, 4, 6, 8, 10, 12, 14]
    ]

    for _ in data:
        print(len(set(_)) == len(_))


if __name__ == "__main__":
    main()
