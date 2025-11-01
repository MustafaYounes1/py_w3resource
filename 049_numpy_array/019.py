"""

Write a NumPy program to find the set difference between two arrays.
The set difference will return sorted, distinct values in array1 that are not in array2.

[0, 10, 20, 40, 60, 80], [10, 30, 40, 50, 70, 90]       -> [ 0 20 60 80]

"""

import numpy as np


def main():
    a, b = [0, 10, 20, 40, 60, 80], [10, 30, 40, 50, 70, 90]
    c = np.setdiff1d(a, b)
    print(c)


if __name__ == "__main__":
    main()
