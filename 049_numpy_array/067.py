"""

Write a NumPy program to sum all the multiples of 3 or 5 below 100.

-> 2318

"""

import numpy as np


def main():
    a = np.arange(1, 100)
    indices = np.logical_or(a % 3 == 0, a % 5 == 0)
    print(a[indices].sum())


if __name__ == "__main__":
    main()
