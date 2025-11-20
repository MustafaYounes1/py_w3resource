"""

Write a NumPy program to sum and compute the product of a numpy array of elements.

input:  np.array([10., 20., 30.])
sum:    60.0
prod:   6000.0

"""

import numpy as np


def main():
    a = np.array([10., 20., 30.])
    print(a.sum())
    print(a.prod())

if __name__ == "__main__":
    main()
