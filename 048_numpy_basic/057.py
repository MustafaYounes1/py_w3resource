"""

Write a NumPy program to multiply two given arrays of the same size element-by-element.

np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.array([[2, 0, 4], [5, 0, 3], [4, 0, 10]])

[[ 2  0 12]
 [20  0 18]
 [28  0 90]]

"""

import numpy as np


def main():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[2, 0, 4], [5, 0, 3], [4, 0, 10]])

    print(a * b)


if __name__ == "__main__":
    main()
