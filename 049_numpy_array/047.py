"""

Write a NumPy program to create an array like the one below.

[[ 2  3  4]
 [ 5  6  7]
 [ 0  9 10]
 [ 0  0 13]]

"""

import numpy as np


def main():
    a = np.arange(2, 14).reshape(4, 3)
    b = np.triu(a, -1)
    print(b)


if __name__ == "__main__":
    main()
