"""

Write a Python program to read a square matrix from the console and print the sum of the matrix's primary diagonal.
Accept the size of the square matrix and elements for each column separated with a space (for every row) as input
from the user.

Input the size of the matrix: 3
2 3 4
4 5 6
3 4 7
Sum of matrix primary diagonal:
14

"""


def main():
    n = int(input("Input the size of the matrix: "))
    data = [list(map(int, input().split())) for _ in range(n)]
    assert all(len(_) == n for _ in data)

    print(sum([data[i][i] for i in range(n)]))


if __name__ == "__main__":
    main()
