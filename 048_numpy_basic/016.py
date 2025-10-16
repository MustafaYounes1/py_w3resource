"""

Write a NumPy program to create a 3x3 identity matrix.

[[1 0 0]
 [0 1 0]
 [0 0 1]]

"""

import numpy as np


def main():
    a = np.identity(3, dtype=int)  # or:    np.eye(3, dtype=int),  np.diag([1] * 3)
    print(a)


if __name__ == "__main__":
    main()
