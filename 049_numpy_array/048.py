"""

Write a NumPy program to collapse a 3-D array into a one-dimensional array.

input:
[[ 1. 0. 0.]
[ 0. 1. 0.]
[ 0. 0. 1.]]

output:
[1. 0. 0. 0. 1. 0. 0. 0. 1.]

"""

import numpy as np


def main():
    a = np.eye(3)
    print(a, "\n")

    b = a.ravel()  # a view of a
    print(b)

if __name__ == "__main__":
    main()
