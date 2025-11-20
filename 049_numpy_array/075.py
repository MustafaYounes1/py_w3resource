"""

Write a NumPy program to create a function cube for all array elements.

input:  [1 2 3 4]
output: [ 1  8 27 64]

"""

import numpy as np


def main():
    a = np.arange(1, 5)
    print(a ** 3)


if __name__ == "__main__":
    main()
