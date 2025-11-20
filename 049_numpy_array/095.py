"""

Write a NumPy program to divide each row by a vector element.

Original array:
array([[20, 20, 20],
       [30, 30, 30],
       [40, 40, 40]])

Vector:
array([20, 30, 40])

output:
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]

"""

import numpy as np


def main():
    a = np.array([[20, 20, 20], [30, 30, 30], [40, 40, 40]])
    b = np.array([20, 30, 40])
    c = a / b[:, None]
    print(c)


if __name__ == "__main__":
    main()
