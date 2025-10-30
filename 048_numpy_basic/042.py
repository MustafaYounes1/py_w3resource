"""

Write a NumPy program to check whether two arrays are equal (element wise) or not.

np.array([0.5, 1.5, 0.2]), np.array([0.4999999999, 1.500000000, 0.2])           -> True

np.array([1, 2, 3]), np.array([1, 2, 3])                                        -> True

np.array([1, 2, 3]), np.array([1, 0, 3])                                        -> False


"""

import numpy as np


def main():
    pairs = [
        [np.array([0.5, 1.5, 0.2]), np.array([0.4999999999, 1.500000000, 0.2])],
        [np.array([1, 2, 3]), np.array([1, 2, 3])],
        [np.array([1, 2, 3]), np.array([1, 0, 3])]
    ]

    for a, b in pairs:
        if np.issubdtype(a.dtype, np.inexact) or np.issubdtype(b.dtype, np.inexact):
            print(np.allclose(a, b))        # use `allclose` for floating-point arrays
        else:
            print(np.array_equal(a, b))     # use `array_equal` otherwise


if __name__ == "__main__":
    main()
