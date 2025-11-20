"""

Write a NumPy program to create an array of (3, 4) shapes, multiply every element value by 3 and display the result array.

input:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

output:
[[ 0  3  6  9]
 [12 15 18 21]
 [24 27 30 33]]

"""

import numpy as np


def main():
    a = np.arange(12).reshape(3, 4)
    print(a * 3)


if __name__ == "__main__":
    main()
