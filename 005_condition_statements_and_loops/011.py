"""

Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

"""


def main():
    n_r, n_c = list(map(int, input("Enter the number of rows and number of columns white-separated: ").split()))
    print([[i * j for j in range(n_c)] for i in range(n_r)])


if __name__ == "__main__":
    main()
