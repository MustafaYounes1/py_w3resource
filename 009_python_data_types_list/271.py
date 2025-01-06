"""

Write a Python program to check if there are duplicate values in a given flat list.

[1, 2, 3, 4, 5, 6, 7]       =>  False
[1, 2, 3, 3, 4, 5, 5, 6, 7] =>  True

"""


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 3, 4, 5, 5, 6, 7]
    ]

    for lst in data:
        print(len(lst) != len(set(lst)))


if __name__ == "__main__":
    main()
