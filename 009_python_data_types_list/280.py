"""

Write a Python program that takes a list of integers and finds all pairs of integers that differ by three.
Return all pairs of integers in a list.

[0, 3, 4, 7, 9]             -> [[0, 3], [4, 7]]
[0, -3, -5, -7, -8]         -> [[-3, 0], [-8, -5]]
[1, 2, 3, 4, 5]             -> [[1, 4], [2, 5]]
[100, 102, 103, 114, 115]   -> [[100, 103]]

"""

from itertools import combinations


def main():
    data = [
        [0, 3, 4, 7, 9],
        [0, -3, -5, -7, -8],
        [1, 2, 3, 4, 5],
        [100, 102, 103, 114, 115]
    ]

    for lst in data:
        print(list(filter(lambda pair: abs(pair[0] - pair[1]) == 3, combinations(lst, 2))))


if __name__ == "__main__":
    main()
