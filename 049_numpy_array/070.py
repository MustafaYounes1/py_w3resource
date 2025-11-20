"""

Write a NumPy program to create the following numpy array:

array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

and print it in fortran order:
    0 4 8 1 5 9 2 6 10 3 7 11

"""

import numpy as np


def main():
    a = np.arange(12).reshape(3, 4)
    print(" ".join(str(x) for x in np.nditer(a, order='F')))


if __name__ == "__main__":
    main()
