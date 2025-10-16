"""

Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.

    [1e10, 1e-7], [1.00001e10, 1e-8]        -> False
    [1e10, 1e-8], [1.00001e10, 1e-9]        -> True
    [1e10, 1e-8], [1.0001e10, 1e-9]         -> False
    [1.0, np.nan], [1.0, np.nan]            -> False    (Considering 'nan's unequal)
    [1.0, np.nan], [1.0, np.nan]            -> True     (Considering 'nan's equal)

Note: Use the NumPy default settings for the absolute/relative tolerance values (atol=1e-08, rtol=1e-05)

"""

import numpy as np


def main():
    arrays = [
        [[1e10, 1e-7], [1.00001e10, 1e-8]],
        [[1e10, 1e-8], [1.00001e10, 1e-9]],
        [[1e10, 1e-8], [1.0001e10, 1e-9]],
        [[1.0, np.nan], [1.0, np.nan]],
        [[1.0, np.nan], [1.0, np.nan]]
    ]

    for (a, b), nan_eq in zip(arrays, [False] * (len(arrays) - 1) + [True]):
        print(np.isclose(a, b, equal_nan=nan_eq).all())


if __name__ == "__main__":
    main()
