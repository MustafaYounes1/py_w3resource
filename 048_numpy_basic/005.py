"""

Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a number).

np.array([-np.inf, 1, 0, np.nan, np.inf])   ->  [False  True  True False False]

"""

import numpy as np


def main():
    a = np.array([-np.inf, 1, 0, np.nan, np.inf])
    print(np.isfinite(a))


if __name__ == "__main__":
    main()
