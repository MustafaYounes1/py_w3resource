"""

Write a NumPy program to find the set exclusive-or of two arrays.
Set exclusive-or will return sorted, distinct values in only one (not both) of the input arrays.

[0, 10, 20, 40, 60, 80], [10, 30, 40, 50, 70]   ->  [ 0 20 30 50 60 70 80]

"""

import numpy as np


def main():
    a, b = [0, 10, 20, 40, 60, 80], [10, 30, 40, 50, 70]
    c = np.setxor1d(a, b)
    print(c)


if __name__ == "__main__":
    main()
