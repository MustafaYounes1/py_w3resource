"""

Write a NumPy program to concatenate two 2-dimensional arrays.

input 1:
[[0 1 3]
 [5 7 9]]

input 2:
[[0 2]
 [6 8]]

output:
[[0 1 3 0 2]
 [5 7 9 6 8]]

"""

import numpy as np


def main():
    a = np.array([[0, 1, 3], [5, 7, 9]])        # (2, 3)
    print(a, "\n")

    b = np.array([[0, 2], [6, 8]])              # (2, 2)
    print(b, "\n")

    c = np.hstack((a, b))                       # (2, 5)
    # or np.concatenate((a, b), axis=1)
    print(c, "\n")


if __name__ == "__main__":
    main()
