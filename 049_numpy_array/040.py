"""

Write a NumPy program to create an array of 10's with the same shape and type as the given array x, where:

     x = np.arange(4, dtype=np.int64)

[10 10 10 10]

"""

import numpy as np


def main():
    x = np.arange(4, dtype=np.int64)
    a = np.full_like(x, fill_value=10)
    assert x.dtype == a.dtype and x.shape == a.shape, "a and x are expected to be of the same type/shape."
    print(a)


if __name__ == "__main__":
    main()
