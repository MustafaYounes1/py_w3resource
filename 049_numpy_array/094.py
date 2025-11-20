"""

Write a NumPy program to check whether the NumPy array is empty or not.

array([])           ->  True
np.array([1, 2])    ->  False

"""

import numpy as np


def main():
    arrays = [
        np.array([]),
        np.array([1, 2])
    ]

    for a in arrays:
        print(a.size == 0)


if __name__ == "__main__":
    main()
