"""

Write a NumPy program to create a 4x4 array.

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

Create an array from said array by swapping first and last, second and third columns.

[[ 3  2  1  0]
 [ 7  6  5  4]
 [11 10  9  8]
 [15 14 13 12]]

"""

import numpy as np


def main():
    a = np.arange(4 * 4).reshape(4, 4)
    print(a, "\n")
    print(np.fliplr(a))


if __name__ == "__main__":
    main()
