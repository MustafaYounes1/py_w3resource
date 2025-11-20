"""

Write a NumPy program to create a NumPy array from a Python Iterator/Generator.

range(10):  [0 1 2 3 4 5 6 7 8 9]

"""

import numpy as np


def main():
    a = np.fromiter(range(10), dtype=int)
    print(a)


if __name__ == "__main__":
    main()
