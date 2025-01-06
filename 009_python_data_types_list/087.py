"""

Write a Python program to read a matrix from the console and print the sum for each column. As input from the user,
accept matrix rows, columns, and elements separated by a space (each row).

Input rows: 2
Input columns: 2
Input number of elements in a row (1, 2, 3):
1 2
3 4
sum for each column:
4 6

"""


def main():
    nr = int(input("Enter the number of rows: "))
    nc = int(input("Enter the number of columns: "))

    data = [list(map(int, input("").split())) for _ in range(nr)]
    assert all(len(_) == nc for _ in data)

    print(
        " ".join(
            list(map(str, [sum([data[i][j] for i in range(nr)]) for j in range(nc)]))
        )
    )


if __name__ == "__main__":
    main()
