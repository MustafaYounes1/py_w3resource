"""

Write a NumPy program to create a 3x3 array with ones on a diagonal and zeros elsewhere.

[[1 0 0]
 [0 1 0]
 [0 0 1]]

"""

import numpy as np


def main():
    a = np.diag([1] * 3)  # np.eye(3), and np.identity(3) also work correctly
    print(a)


if __name__ == "__main__":
    main()
