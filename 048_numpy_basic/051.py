"""

Write a NumPy program to extract all numbers from a given array less and greater than a specified number.

np.array([[5.54, 3.38, 7.99],
          [3.54, 4.38, 6.99],
          [1.54, 2.39, 9.29]])

> 5     -> [5.54 7.99 6.99 9.29]
< 6     -> [5.54 3.38 3.54 4.38 1.54 2.39]

"""

import numpy as np


def main():
    a = np.array([[5.54, 3.38, 7.99],
                  [3.54, 4.38, 6.99],
                  [1.54, 2.39, 9.29]])

    print(a[a>5])
    print(a[a<6])

if __name__ == "__main__":
    main()
