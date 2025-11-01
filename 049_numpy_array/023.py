"""

Write a NumPy program to test whether any array element along a given axis evaluates to True.

[[0 1 2]
 [0 0 0]]

Test along rows:
[ True False]

Test along columns:
[False  True  True]

"""

import numpy as np


def main():
    a = np.array([[0, 1, 2], [0, 0, 0]])

    print(f"Test along rows:")
    print(a.any(axis=1), "\n")

    print(f"Test along columns:")
    print(a.any(axis=0))

if __name__ == "__main__":
    main()
