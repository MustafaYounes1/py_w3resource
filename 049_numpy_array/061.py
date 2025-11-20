"""

Write a NumPy program that splits an array of shape 4x4 into two arrays along the second axis.

np.array([[ 0,  1,  2,  3],
          [ 4,  5,  6,  7],
          [ 8,  9, 10, 11],
          [12, 13, 14, 15]])

output:
[[ 0  1]
 [ 4  5]
 [ 8  9]
 [12 13]]

[[ 2  3]
 [ 6  7]
 [10 11]
 [14 15]]

"""

import numpy as np


def main():
    a = np.arange(16).reshape(4, 4)
    a1, a2 = np.split(a, 2, axis=1)
    print(a1, a2, sep='\n')


if __name__ == "__main__":
    main()
