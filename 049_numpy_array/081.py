"""

Write a NumPy program to convert a NumPy array of floating values to a numpy array of integer values.

Original array elements:
array([[12.  , 12.51],
       [ 2.34,  7.98],
       [25.23, 36.5 ]])

Convert float values to intger values:
[[12 12]
 [ 2  7]
 [25 36]]

"""

import numpy as np


def main():
    a = np.array([[12.  , 12.51],
                  [ 2.34,  7.98],
                  [25.23, 36.5 ]])
    b = a.astype(int)
    print(b)


if __name__ == "__main__":
    main()
