"""

Write a NumPy program to test element-wise for NaN of a given array.

np.array([-np.inf, 1, 0, np.nan, np.inf])   ->  [False False False  True False]

"""

import numpy as np


def main():
    a = np.array([-np.inf, 1, 0, np.nan, np.inf])
    print(np.isnan(a))


if __name__ == "__main__":
    main()
