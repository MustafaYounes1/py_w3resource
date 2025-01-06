"""

Write a Python program to check whether a specified list is sorted or not.

[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]     =>  True
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]     =>  True

"""


def main():
    data = [
        [1, 2, 4, 6, 8, 10, 12, 14, 16, 17],
        [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
    ]

    for _ in data:
        print(sorted(_) == _)


if __name__ == "__main__":
    main()
