"""

Write a NumPy program to suppress the use of scientific notation for small numbers in a NumPy array.

input:      array([1.60e-10, 1.60e-08, 1.60e+00, 1.20e+03, 2.35e-01])
output:     [   0.            0.00000002    1.6        1200.            0.235     ]

"""

import numpy as np


def main():
    a = np.array([1.60000000e-10, 1.60000000e-08, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01])

    # print floating point numbers using fixed point notation, in which case numbers equal to zero in the
    # current precision (8 by default) will print as zero.
    with np.printoptions(suppress=True):
        print(a)


if __name__ == "__main__":
    main()
