"""

Create a 5x5 list of lists with row values ranging from 0 to 4

Output: [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

"""


def main():
    print(
        [list(range(5)) for _ in range(5)]
    )


if __name__ == "__main__":
    main()
