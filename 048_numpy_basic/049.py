"""

Write a NumPy program to create a new integer array of shape (5, 6) filled with zeros.

[[0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]]

"""

import numpy as np


def main():
    a = np.zeros((5, 6), dtype=int)
    print(a)


if __name__ == "__main__":
    main()
