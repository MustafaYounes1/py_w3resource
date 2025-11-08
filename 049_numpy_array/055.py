"""

Write a NumPy program to insert a new axis within a 2-D array.

input shape:    (3, 4)
output shape:   (3, 1, 4)

Note: you may work on an array filled with ones

"""

import numpy as np


def main():
    a = np.ones((3, 4))
    b = np.expand_dims(a, axis=1)       # or b = a[:, np.newaxis, :]
    print(f"{a.shape} -> {b.shape}")


if __name__ == "__main__":
    main()
