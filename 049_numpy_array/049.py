"""

Write a NumPy program to find the 4th element of a specified array.

Input:
[[ 2 4 6]
[ 6 8 10]]

output:
6

"""

import numpy as np


def main():
    a = np.array([[2, 4, 6], [6, 8, 10]])
    print(a, "\n")
    print(a.flat[3])


if __name__ == "__main__":
    main()
