"""

Write a NumPy program to create a 5x5 array with 1 on the border and 0 inside.

[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]

"""

import numpy as np


def main():
    a = np.pad(np.zeros((3, 3), dtype=int), pad_width=1, constant_values=1)

    # or
    # a = np.ones((5, 5), dtype=int)
    # a[1:-1, 1:-1] = 0

    print(a)

if __name__ == "__main__":
    main()
