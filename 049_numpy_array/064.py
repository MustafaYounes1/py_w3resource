"""

Write a NumPy program to test whether specified values are present in an array.

np.array([[1.12, 2.  , 3.45],
          [2.33, 5.12, 6.  ]])

2       -> True
0       -> False
6       -> True
2.3     -> False
5.12    -> True

"""

import numpy as np


def main():
    a = np.array([[1.12, 2.0, 3.45], [2.33, 5.12, 6.0]])
    b = np.isin([2, 0, 6, 2.3, 5.12], a, assume_unique=True)
    print(b)


if __name__ == "__main__":
    main()
