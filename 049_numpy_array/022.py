"""

Write a NumPy program to test whether all elements in an array evaluate to True.

[[0, 0], [0, 0]]        ->      False
[[0, 1], [2, 3]]        ->      False
[[1, 2], [3, 4]]        ->      True

"""

import numpy as np


def main():
    arrays = [
        [[0, 0], [0, 0]],
        [[0, 1], [2, 3]],
        [[1, 2], [3, 4]]
    ]

    for a in arrays:
        print(np.asarray(a).all())


if __name__ == "__main__":
    main()
