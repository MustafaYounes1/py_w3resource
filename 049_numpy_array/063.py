"""

Write a NumPy program to create a 5x5 matrix with row values ranging from 0 to 4.

[[0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]
 [0 1 2 3 4]]

"""

import numpy as np


def main():
    a = np.broadcast_to(np.arange(5), (5, 5))
    print(a)


if __name__ == "__main__":
    main()
