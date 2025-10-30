"""

Write a NumPy program to add a vector to each row of a given matrix.

The input matrix:
array([[4, 3, 6, 0, 5, 4],
       [6, 2, 7, 5, 0, 4],
       [5, 9, 4, 0, 4, 3],
       [1, 1, 8, 1, 2, 8],
       [2, 8, 1, 1, 3, 3]])

The input vector:
array([ 3,  2,  2, -2, -1, -1])

out:
[[ 7  5  8 -2  4  3]
 [ 9  4  9  3 -1  3]
 [ 8 11  6 -2  3  2]
 [ 4  3 10 -1  1  7]
 [ 5 10  3 -1  2  2]]

"""

import numpy as np


def main():
    a = np.array([[4, 3, 6, 0, 5, 4],           # (5, 6)
                  [6, 2, 7, 5, 0, 4],
                  [5, 9, 4, 0, 4, 3],
                  [1, 1, 8, 1, 2, 8],
                  [2, 8, 1, 1, 3, 3]])

    v = np.array([ 3,  2,  2, -2, -1, -1])      # (6,)

    print(a + v)


if __name__ == "__main__":
    main()
