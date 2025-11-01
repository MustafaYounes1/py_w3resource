"""

Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.

Original array:

np.array([[0, 10, 20], [20, 30, 40]])

Values bigger than 10       [20 20 30 40]
Their indices are           (array([0, 1, 1, 1]), array([2, 0, 1, 2]))

"""

import numpy as np


def main():
    a = np.array([[0, 10, 20], [20, 30, 40]])
    indices = (a > 10).nonzero()
    print(a[indices])
    print(indices)

if __name__ == "__main__":
    main()
