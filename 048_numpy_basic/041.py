"""

Write a NumPy program to conditionally add elements in a given 2d array .

If an element in the matrix is 0, we will not add the element below this element.

np.array([[1, 1, 0, 2],
          [0, 3, 0, 3],
          [1, 0, 4, 4]])

-> 14 (exclude the first/third numbers in the last row since the number above are zeros)

"""

import numpy as np


def main():
    a = np.array([[1, 1, 0, 2],
                  [0, 3, 0, 3],
                  [1, 0, 4, 4]])

    b = a.copy()                        # don't modify the original array
    ir, ic = np.where(b[:-1] == 0)      # indices of zeros (excluding the last row)
    ir = np.array(ir) + 1               # increase the row indices by one to get the row index of the number below
    b[ir, ic] = 0                       # set the numbers in the row below to zero
    print(b.sum())


if __name__ == "__main__":
    main()
