"""

Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range
from 9 to 15.

[  0   1   2   3   4   5   6   7   8  -9 -10 -11 -12 -13 -14 -15  16  17
  18  19  20]

"""

import numpy as np


def main():
    a = np.arange(21)
    a[9:16] *= -1
    print(a)


if __name__ == "__main__":
    main()
