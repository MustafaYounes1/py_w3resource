"""

Write a NumPy program to multiply the values (element-wise) of two given vectors.

np.array([1, 8, 3, 5])
np.array([1, 6, 4, 6])

    -> [ 1 48 12 30]

"""

import numpy as np


def main():
    a, b = np.array([1, 8, 3, 5]), np.array([1, 6, 4, 6])
    print(a * b)


if __name__ == "__main__":
    main()
