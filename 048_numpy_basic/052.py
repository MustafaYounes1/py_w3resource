"""

Write a NumPy program to replace all numbers in a given array equal, less and greater than a given number.

np.array([[5.54, 3.38, 7.99],
          [3.54, 4.38, 6.99],
          [1.54, 2.39, 9.29]])

numbers > 6 are replaced with positive infinity
numbers < 3 are replaced with negative infinity

[[5.54 3.38  inf]
 [3.54 4.38  inf]
 [-inf -inf  inf]]

"""

import numpy as np


def main():
    a = np.array([[5.54, 3.38, 7.99],
                  [3.54, 4.38, 6.99],
                  [1.54, 2.39, 9.29]])

    a[a>6] = np.inf
    a[a<3] = -np.inf

    print(a)


if __name__ == "__main__":
    main()
