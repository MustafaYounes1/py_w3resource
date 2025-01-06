"""

Create a 3x3 list of lists with values ranging from 0 to 8.

Output: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

"""


def main():
    print(
        [[i, i + 1, i + 2] for i in range(0, 9, 3)]
    )


if __name__ == "__main__":
    main()
