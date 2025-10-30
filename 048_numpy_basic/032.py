"""

Write a NumPy program to compute the inner product of two given vectors.

x = np.array([4, 5])
y = np.array([7, 10])

-> 78

"""

import numpy as np


def main():
    x = np.array([4, 5])
    y = np.array([7, 10])
    print(np.inner(x, y))         # 'np.dot(x, y)' and 'x @ y' also work


if __name__ == "__main__":
    main()
