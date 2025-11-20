"""

Write a NumPy program to replace the negative values in a NumPy array with 0.

Original array:
array([-1, -4,  0,  2,  3,  4,  5, -6])

Replace the negative values of the said array with 0:
[0 0 0 2 3 4 5 0]

"""

import numpy as np


def main():
    a = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
    print(repr(a))
    a[a < 0] = 0
    print(a)


if __name__ == "__main__":
    main()
