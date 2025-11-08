"""

Write a NumPy program to remove single-dimensional entries from a specified shape.

input shape:    (3, 1, 4)
output shape:   (3, 4)

Note: you may work on an array filled with ones

"""

import numpy as np


def main():
    a = np.ones((3, 1, 4))
    b = np.squeeze(a)
    print(f"{a.shape} -> {b.shape}")


if __name__ == "__main__":
    main()
