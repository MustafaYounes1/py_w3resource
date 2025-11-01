"""

Write a NumPy program to compare two arrays using NumPy.

a: [1 2]
b: [4 5]

a greater than b        [False False]
a less than b           [ True  True]

"""

import numpy as np


def main():
    a, b = np.array([1, 2]), np.array([4, 5])
    print(f"a>b:      {a>b}")
    print(f"a<b:      {a<b}")


if __name__ == "__main__":
    main()
