"""

Write a NumPy program to find the number of rows and columns in a given matrix.

np.array([[ 0,  1,  2,  3,  4,  5,  6,  7],
          [ 8,  9, 10, 11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20, 21, 22, 23]])

-> (3, 8)

"""

import numpy as np


def main():
    a = np.array([[ 0,  1,  2,  3,  4,  5,  6,  7],
                  [ 8,  9, 10, 11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20, 21, 22, 23]])

    print(a.shape)


if __name__ == "__main__":
    main()
