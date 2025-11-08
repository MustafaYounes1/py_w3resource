"""

Write a NumPy program to create an array like the one below.

[[0. 0. 0.]
 [1. 0. 0.]
 [1. 1. 0.]
 [1. 1. 1.]]

"""

import numpy as np


def main():
    a = np.tri(4, 3, -1)
    print(a)


if __name__ == "__main__":
    main()
