"""

Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.

[[1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]
 [0 0 0 0 5]]

"""

import numpy as np


def main():
    a = np.diag([1, 2, 3, 4, 5])
    print(a)


if __name__ == "__main__":
    main()
