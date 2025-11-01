"""

Write a NumPy program to change an array's dimension.

a: original (24,)
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

b: (4, 6)
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]

c: (2, 2, 3, 2)
[[[[ 0  1]
   [ 2  3]
   [ 4  5]]

  [[ 6  7]
   [ 8  9]
   [10 11]]]


 [[[12 13]
   [14 15]
   [16 17]]

  [[18 19]
   [20 21]
   [22 23]]]]

"""

import numpy as np


def main():
    a = np.arange(4*6)
    print(a, "\n")

    b = a.reshape(4, 6)
    print(b, "\n")

    c = b.reshape(2, 2, 3, 2)
    print(c, "\n")


if __name__ == "__main__":
    main()
