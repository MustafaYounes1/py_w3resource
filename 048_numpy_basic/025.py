"""

Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

[[10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]]

"""

import numpy as np


def main():
    a = np.arange(10, 22).reshape(3, 4)
    print(a)


if __name__ == "__main__":
    main()
