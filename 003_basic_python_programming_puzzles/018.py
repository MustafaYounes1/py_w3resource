"""

An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row.
Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them,
but they are useful as arrays in computing.

Write a Python program to find the indices of all occurrences of target in the uneven matrix.

Input:
[([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]), 19]
Output:
[[0, 4], [1, 0], [1, 3], [4, 1]]

Input:
[([1, 2, 3, 2], [], [7, 9, 2, 1, 4]), 2]
Output:
[[0, 1], [0, 3], [2, 2]]

"""


__data = [
    [([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]), 19],
    [([1, 2, 3, 2], [], [7, 9, 2, 1, 4]), 2]
]


def main():
    for arr, n in __data:
        print(
            [
                [i, j] for i, row in enumerate(arr) for j, _ in enumerate(row) if _ == n
            ]
        )


if __name__ == "__main__":
    main()
