"""

Write a NumPy program to get native python items from numpy arrays.

"""

import numpy as np


def main():
    a = np.arange(9).reshape(3, 3)
    i = a.item(0, 1)
    assert isinstance(i, int)


if __name__ == "__main__":
    main()
