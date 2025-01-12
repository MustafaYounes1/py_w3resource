"""

Write a Python program to compare two unordered lists (not sets).

[20, 10, 30, 10, 20, 30]
[30, 20, 10, 30, 20, 50]

False

[1, 2, 3]
[2, 1, 3]

True

"""

from collections import Counter


def main():
    data = [
        [
            [20, 10, 30, 10, 20, 30],
            [30, 20, 10, 30, 20, 50]
        ],
        [
            [1, 2, 3],
            [2, 1, 3]
        ]
    ]

    for lst1, lst2 in data:
        print(Counter(lst1) == Counter(lst2))


if __name__ == "__main__":
    main()
