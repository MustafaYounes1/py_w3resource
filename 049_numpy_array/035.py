"""

Write a NumPy program to create a contiguous flattened array.

Original array:

[[10 20 30]
[20 40 50]]

New flattened array:
[10 20 30 20 40 50]

"""

import numpy as np


def main():
    a = np.array([[10, 20, 30], [20, 40, 50]])
    print(a, "\n")
    print(a.ravel())


if __name__ == "__main__":
    main()
