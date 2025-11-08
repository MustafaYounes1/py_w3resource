"""

Write a NumPy program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere.

[[4 0 0 0]
 [0 5 0 0]
 [0 0 6 0]
 [0 0 0 8]]

"""

import numpy as np


def main():
    a = np.diag([4, 5, 6, 8])   # or diagflat can also work
    print(a)


if __name__ == "__main__":
    main()
