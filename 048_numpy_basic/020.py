"""

Write a NumPy program to create a 3x4 array (ranging from 0 to 11) and iterate over it.

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

(0, 0) 0
(0, 1) 1
(0, 2) 2
(0, 3) 3
(1, 0) 4
(1, 1) 5
(1, 2) 6
(1, 3) 7
(2, 0) 8
(2, 1) 9
(2, 2) 10
(2, 3) 11

"""

import numpy as np


def main():
    a = np.arange(12).reshape(3, 4)
    print(a)

    for idx, val in np.ndenumerate(a):
        print(idx, val)


if __name__ == "__main__":
    main()
