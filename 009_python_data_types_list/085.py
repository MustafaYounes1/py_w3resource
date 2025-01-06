"""

Write a Python program to create a multidimensional list (lists of lists) with zeros.

[[0, 0], [0, 0], [0, 0]]

"""


def main():
    print(
        [[0 for _ in range(2)] for _ in range(3)]
    )


if __name__ == "__main__":
    main()
