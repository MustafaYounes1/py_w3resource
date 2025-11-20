"""

Write a NumPy program to create an array with 10^3 evenly spaced elements (starting from zero).

"""

import numpy as np


def main():
    a = np.arange(10**3)
    print(a.size == 1e3)


if __name__ == "__main__":
    main()
