"""

Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

"""

import numpy as np


def main():
    a = np.zeros(10)
    a[5] = 11
    print(a)


if __name__ == "__main__":
    main()
