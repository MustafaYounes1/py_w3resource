"""

Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge,
when starting from the top and proceeding according to the next rule to the bottom. Write a Python program that
compute the maximum value of the sum of the passing integers according to the following rules.

At each step, you can go to the lower left diagonal or the lower right diagonal. For example, in the example of FIG. 1,
as shown in FIG. 2, when 8,4,9,8,6,8,9,4,8 is selected and passed, the sum is 64
(8 + 4 + 9) + 8 + 6 + 8 + 9 + 4 + 8 = 64)

Input:
A series of integers separated by commas are given in diamonds. No spaces are included in each line.
The input example corresponds to Figure 1. The number of lines of data is less than 100 lines.

Example1:
        [8],                        => 64
        [4, 9],
        [9, 2, 1],
        [3, 8, 5, 5],
        [5, 6, 3, 7, 6],
        [3, 8, 5, 5],
        [9, 2, 1],
        [4, 9],
        [8]

Example2:
        [7],                          => 55
        [3, 8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5],
        [2, 7, 4, 4],
        [8, 1, 0],
        [3, 8],
        [7]


"""

# read user input from sys.stdin and close the stream when pressing ctrl+d
import sys


def main():
    # hardcoded
    data = [
        [8],
        [4, 9],
        [9, 2, 1],
        [3, 8, 5, 5],
        [5, 6, 3, 7, 6],
        [3, 8, 5, 5],
        [9, 2, 1],
        [4, 9],
        [8]
    ]

    # data = [
    #     [7],
    #     [3, 8],
    #     [8, 1, 0],
    #     [2, 7, 4, 4],
    #     [4, 5, 2, 6, 5],
    #     [2, 7, 4, 4],
    #     [8, 1, 0],
    #     [3, 8],
    #     [7]
    # ]

    # prompting the user to provide data using sys.stdin
    # data = [list(map(int, line.split(","))) for line in sys.stdin]

    # Initialize the maximum value vector with the first row of input
    mvv = data[0]

    # Iterate over the remaining rows in a pyramid fashion to find the maximum path sum
    for i in range(1, len(data) // 2 + 1):
        # store the current maximum sums till this row
        rvv = [0] * (i + 1)
        for j in range(i):
            rvv[j] = max(rvv[j], mvv[j] + data[i][j])
            rvv[j + 1] = max(rvv[j + 1], mvv[j] + data[i][j + 1])

        mvv = rvv

    # Continue iterating over the remaining rows in a reversed pyramid fashion
    for i in range(len(data) // 2 + 1, len(data)):
        # store the current maximum sums till this row
        rvv = [0] * (len(mvv) - 1)
        for j in range(len(rvv)):
            rvv[j] = max(mvv[j], mvv[j+1]) + data[i][j]

        mvv = rvv

    print(mvv[0])


if __name__ == "__main__":
    main()
