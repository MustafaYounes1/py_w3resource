"""

Your task is to develop a small part of spreadsheet software.
Write a Python program that adds up the columns and rows of the given table as shown in the specified figure:

n (the size of row and column of the given table)
1st row of the table
2nd row of the table
:
:
n th row of the table
The input ends with a line consisting of a single 0.
Output:
For each dataset, print the table with sum of rows and columns.

Input number of rows/columns (0 to exit)
 4
Input cell value:
 25 69 51 26
 68 35 29 54
 54 57 45 63
 61 68 47 59
Result:
   25   69   51   26  171
   68   35   29   54  186
   54   57   45   63  219
   61   68   47   59  235
  208  229  172  202  811
Input number of rows/columns (0 to exit)

"""


def main():
    n = int(input("Input number of rows/columns: "))
    data = []

    for _ in range(n):
        data.append(list(map(int, input("").split())))

    for i in range(len(data)):
        # sum of the row
        data[i].append(sum(data[i]))

    # store the columns sum in the last row
    data.append([])

    for i in range(len(data) - 1):
        # sum of the column
        data[-1].append(sum([row[i] for row in data[:-1]]))

    data[-1].append(sum([row[-1] for row in data[:-1]]))

    for row in data:
        print("".join(list(map(lambda x: "%4s" % str(x), row))))


if __name__ == "__main__":
    main()
