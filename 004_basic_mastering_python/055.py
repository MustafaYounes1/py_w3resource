"""

Transpose a 2D list.

e.g. matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]     =>  [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

"""


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(
        [list(_) for _ in zip(*matrix)]
    )


if __name__ == "__main__":
    main()
