"""

Write a NumPy program to create a 3x3 int16 array of ones and a 4x2 float16 array of zeros.

[[1 1 1]
 [1 1 1]
 [1 1 1]]

[[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]]

"""

import numpy as np


def main():
    a = np.ones((3, 3), dtype=np.int16)
    print(a, "\n")

    b = np.zeros((4, 2), dtype=np.float16)
    print(b)


if __name__ == "__main__":
    main()
