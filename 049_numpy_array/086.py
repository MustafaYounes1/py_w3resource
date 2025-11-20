"""

Write a NumPy program to find distinct rows in a NumPy array.

array([[20, 20, 20,  0],
       [ 0, 20, 20, 20],
       [ 0, 20, 20, 20],
       [20, 20, 20,  0],
       [10, 20, 20, 20]])

output:
[[ 0 20 20 20]
 [10 20 20 20]
 [20 20 20  0]]

"""

import numpy as np


def main():
    a = np.array([[20, 20, 20,  0],
                  [ 0, 20, 20, 20],
                  [ 0, 20, 20, 20],
                  [20, 20, 20,  0],
                  [10, 20, 20, 20]])
    rows = np.unique(a, axis=0)
    print(rows)

if __name__ == "__main__":
    main()
