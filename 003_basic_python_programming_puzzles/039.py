"""

Write a Python program to determine which triples sum to zero from a given list of lists.

Input: [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
Output:
[False, True, True, False, True]

Input: [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]
Output:
[True, True, False, False, False]

"""

__data = [
    [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]],
    [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]
]


def main():
    for sample in __data:
        print([sum(_) == 0 for _ in sample])


if __name__ == "__main__":
    main()
