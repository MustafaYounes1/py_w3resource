"""

Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives (of int64 type).

[0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5]

"""

import numpy as np


def main():
    a = np.r_[[0] * 10, [1] * 10, [5] * 10]
    print(a)


if __name__ == "__main__":
    main()
