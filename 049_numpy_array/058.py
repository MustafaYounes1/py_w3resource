"""

Write a NumPy program to convert 1-D arrays as columns into a 2-D array.

input 1: [10 20 30]
input 2: [40 50 60]

output:         (shape (3, 2))
[[10 40]
 [20 50]
 [30 60]]

"""

import numpy as np


def main():
    a, b = np.arange(10, 40, 10), np.arange(40, 70, 10)     # each of shape (3,)
    print(a)
    print(b, "\n")

    c = np.column_stack((a, b))                             # (3, 2)
    # or np.stack((a, b), axis=-1)
    print(c)

if __name__ == "__main__":
    main()
