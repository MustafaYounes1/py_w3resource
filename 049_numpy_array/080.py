"""

Write a NumPy program to access an array by column.

array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

column 1: [0 3 6]
column 2: [1 4 7]
column 3: [2 5 8]

"""

import numpy as np


def main():
    a = np.arange(9).reshape(3, 3)

    for j in range(a.shape[1]):
        print(f"column {j+1}: {a[:, j]}")


if __name__ == "__main__":
    main()
