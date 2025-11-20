"""

Write a NumPy program to add an extra column to a NumPy array.

the array:
array([[10, 20, 30],
       [40, 50, 60]])

the column:
[100, 200]

output:
[[ 10  20  30 100]
 [ 40  50  60 200]]

"""

import numpy as np


def main():
    a = np.arange(10, 70, 10).reshape(2, 3)
    column = [100, 200]
    b = np.column_stack((a, column))
    print(b)


if __name__ == "__main__":
    main()
