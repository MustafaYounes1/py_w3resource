"""

Write a Python program to compare two given lists and find the indices (w.r.t the first list) of the values present
in both lists.

[1, 2, 3, 4, 5, 6]
[7, 8, 5, 2, 10, 12]
[1, 4]

[1, 2, 3, 4, 5, 6]
[7, 8, 5, 7, 10, 12]
[4]

[1, 2, 3, 4, 15, 6]
[7, 8, 5, 7, 10, 12]
[]

"""


def main():
    data = [
        [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 5, 2, 10, 12]
        ],
        [
            [1, 2, 3, 4, 5, 6],
            [7, 8, 5, 7, 10, 12]
        ],
        [
            [1, 2, 3, 4, 15, 6],
            [7, 8, 5, 7, 10, 12]
        ]
    ]

    for lst1, lst2 in data:
        print([idx for idx, _ in enumerate(lst1) if _ in lst2])


if __name__ == "__main__":
    main()
