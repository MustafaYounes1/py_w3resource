"""

Write a NumPy program to find the union of two arrays.
Union will return a unique, sorted array of values in each of the two input arrays.

[0, 10, 20, 40, 60, 80], [10, 30, 40, 50, 70]       ->  [ 0 10 20 30 40 50 60 70 80]

"""

import numpy as np


def main():
    a, b = [0, 10, 20, 40, 60, 80], [10, 30, 40, 50, 70]
    c = np.union1d(a, b)
    print(c)


if __name__ == "__main__":
    main()
