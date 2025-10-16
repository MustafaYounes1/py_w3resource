"""

Write a NumPy program to test if any of the elements of a given array are non-zero.

np.array([1, 2, 3, 4])  ->  True
np.array([0, 1, 2, 3])  ->  True
np.array([0, 0])        ->  False

"""

import numpy as np


def main():
    arrays = [np.array([1, 2, 3, 4]), np.array([0, 1, 2, 3]), np.array([0, 0])]

    for arr in arrays:
        print(arr.any())


if __name__ == "__main__":
    main()
