"""

Write a NumPy program to find common values between two arrays.

[0, 10, 20, 40, 60], [10, 30, 40]       ->  [10 40]

"""

import numpy as np


def main():
    a, b = [0, 10, 20, 40, 60], [10, 30, 40]
    c = np.intersect1d(a, b)
    print(c)


if __name__ == "__main__":
    main()
