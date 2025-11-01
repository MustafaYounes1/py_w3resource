"""

Write a NumPy program to get the unique elements of an array.

[10 10 20 20 30 30]
    -> [10 20 30]

[[1 1]
[2 3]]
    -> [1 2 3]

"""

import numpy as np


def main():
    arrays = [
        [10, 10, 20, 20, 30, 30],
        [[1, 1], [2, 3]]
    ]

    for a in arrays:
        print(np.unique(a))


if __name__ == "__main__":
    main()
