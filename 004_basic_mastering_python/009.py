"""

Calculate the sum of the diagonal elements of a 3x3 matrix (list of lists).

e.g.    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]      =>  15
"""


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(
        sum(
            [el for (j, row) in enumerate(matrix) for (i, el) in enumerate(row) if i == j]
        )
    )


if __name__ == "__main__":
    main()
