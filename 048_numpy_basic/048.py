"""

Write a NumPy program to create a 4x4 array with random values.

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

Create an array from the said array swapping first and last rows.

[[12 13 14 15]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [ 0  1  2  3]]

"""

import numpy as np


def main():
    a = np.arange(4 * 4).reshape(4, 4)

    b = a.copy()
    b[[0, -1]] = b[[-1, 0]]
    print(b)


if __name__ == "__main__":
    main()
