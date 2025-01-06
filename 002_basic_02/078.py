"""

Write a Python program to print a given N by M matrix of numbers line by line in forward > backwards > forward >...
order.

Input matrix:
[[1, 2, 3,4],
[5, 6, 7, 8],
[0, 6, 2, 8],
[2, 3, 0, 2]]

Output:
1
2
3
4
8
7
6
5
0
6
2
8
2
0
3
2

"""


def main():
    # hardcoded
    data = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [0, 6, 2, 8],
        [2, 3, 0, 2]
    ]

    # prompting the user
    # n_rows = int(input("Enter the number of rows: "))
    # data = [list(map(int, input().split())) for _ in range(n_rows)]

    for idx, row in enumerate(data):
        start, step = (0, 1) if idx % 2 == 0 else (-1, -1)
        for _ in row[start::step]:
            print(_)


if __name__ == "__main__":
    main()
