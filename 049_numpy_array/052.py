"""

Write a NumPy program to move the specified axis backwards, until it lies in a given position.

input shape:    (2, 3, 4, 5)
output shape:   (2, 5, 3, 4)

Note: you may do this on an array filled of ones

"""

import numpy as np


def main():
    a = np.ones((2, 3, 4, 5))
    b = np.moveaxis(a, -1, 1)
    print(f"{a.shape} -> {b.shape}")


if __name__ == "__main__":
    main()
