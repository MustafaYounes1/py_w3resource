"""

Write a NumPy program to move array axes to alternate positions.

Other axes remain in their original order.

Input:          (shape is (3, 4, 1, 2))
[[[[ 0  1]]

  [[ 2  3]]

  [[ 4  5]]

  [[ 6  7]]]


 [[[ 8  9]]

  [[10 11]]

  [[12 13]]

  [[14 15]]]


 [[[16 17]]

  [[18 19]]

  [[20 21]]

  [[22 23]]]]

Output:         (shape is (4, 2, 1, 3))
[[[[ 0  8 16]]

  [[ 1  9 17]]]


 [[[ 2 10 18]]

  [[ 3 11 19]]]


 [[[ 4 12 20]]

  [[ 5 13 21]]]


 [[[ 6 14 22]]

  [[ 7 15 23]]]]

"""

import numpy as np


def main():
    a = np.arange(3*4*2).reshape(3, 4, 1, 2)
    print(a, a.shape, "\n")

    b = np.transpose(a, (1, 3, 2, 0))
    print(b, b.shape)


if __name__ == "__main__":
    main()
