"""

Write a NumPy program to create an array of equal shape and data type for a given array.

The input array:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]

 Output array: the same shape/type as the input array filled with 5s
[[5 5 5 5 5]
 [5 5 5 5 5]
 [5 5 5 5 5]
 [5 5 5 5 5]
 [5 5 5 5 5]]

"""

import numpy as np


def main():
    a = np.arange(25).reshape(5, 5)
    print(a, "\n")

    b = np.full_like(a, 5)
    print(b)


if __name__ == "__main__":
    main()
