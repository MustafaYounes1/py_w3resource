"""

Write a NumPy program to test whether none of the elements of a given array are zero.

np.array([1, 2, 3, 4])  ->  True
np.array([0, 1, 2, 3])  ->  False

"""

import numpy as np


def main():
    arrays = [np.array([1, 2, 3, 4]), np.array([0, 1, 2, 3])]

    for arr in arrays:
        print(arr.all())


if __name__ == "__main__":
    main()
