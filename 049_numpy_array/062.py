"""

Write a NumPy program to get the number of non-zero elements in an array.

np.array([[ 0, 10, 20],
          [20, 30, 40]])

-> 5

"""

import numpy as np


def main():
    a = np.array([[ 0, 10, 20],
                  [20, 30, 40]])

    print(np.count_nonzero(a))


if __name__ == "__main__":
    main()
