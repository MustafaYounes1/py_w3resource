"""

Write a NumPy program to create an array of all even integers from 30 to 70.

[30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70]

"""

import numpy as np


def main():
    a = np.arange(30, 71, 2)
    print(a)


if __name__ == "__main__":
    main()
