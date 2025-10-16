"""

Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.

[[1 1 1 1 1 1 1 1 1 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 1 1 1 1 1 1 1 1 1]]

"""

import numpy as np


def main():
    a = np.pad(np.zeros((8, 8), dtype=int), pad_width=1, mode='constant', constant_values=1)
    print(a)


if __name__ == "__main__":
    main()
