"""

Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

[0, 10, 20, 40, 60], [0, 40]    -> [ True False False  True False]

"""

import numpy as np


def main():
    a, b = [0, 10, 20, 40, 60], [0, 40]
    c = np.isin(a, b)
    print(c)


if __name__ == "__main__":
    main()
