"""

Create a 3x3 identity matrix as a list of lists.

output:    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

"""


def main():
    print(
        [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    )


if __name__ == "__main__":
    main()
