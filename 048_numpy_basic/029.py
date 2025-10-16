"""

Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.

[[0 1 0 1]
 [1 0 1 0]
 [0 1 0 1]
 [1 0 1 0]]

"""

import numpy as np


def main():
    a = np.ones((4, 4), dtype=int)
    a[::2, ::2] = 0
    a[1::2, 1::2] = 0
    print(a)



if __name__ == "__main__":
    main()
