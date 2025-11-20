"""

Write a NumPy program to remove all rows in a NumPy array that contain non-numeric values.

Original array:
array([[ 1.,  2.,  3.],
       [ 4.,  5., nan],
       [ 7.,  8.,  9.],
       [ 1.,  0.,  1.]])

Remove all non-numeric elements of the said array
[[1. 2. 3.]
 [7. 8. 9.]
 [1. 0. 1.]]

"""

import numpy as np


def main():
    a = np.array([[ 1.,  2.,  3.],
                  [ 4.,  5., np.nan],
                  [ 7.,  8.,  9.],
                  [ 1.,  0.,  1.]])

    b = np.delete(a, np.isnan(a).any(axis=-1), 0)
    print(b)

if __name__ == "__main__":
    main()
