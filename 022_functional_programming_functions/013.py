"""

Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
Each number is the two numbers above it added together.

pascal_triangle(6)

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]

"""


def pascal_triangle(n: int) -> list[list[int]]:
    res: list[list[int]] = []

    for _ in range(n):
        if _ == 0:
            res += [[1]]

        else:
            res += [[1] + list(map(sum, zip(res[-1][:-1], res[-1][1:]))) + [1]]

    return res


def main():
    for _ in pascal_triangle(6):
        print(_)


if __name__ == "__main__":
    main()
