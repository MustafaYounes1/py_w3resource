"""

Create a 5x5 list with 1 on the border and 0 inside.

Output: [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

"""


def main():
    print(
        [[1 if i in (0, 4) or j in (0, 4) else 0 for j in range(5)] for i in range(5)]
    )


if __name__ == "__main__":
    main()
