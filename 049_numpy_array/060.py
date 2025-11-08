"""

Write a NumPy program to split an array of 14 elements into 3 arrays, each with 2, 4, and 8 elements in the original order.

input: [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14]

output:
[array([1, 2]), array([3, 4, 5, 6]), array([ 7, 8, 9, 10, 11, 12, 13, 14])]

"""

import numpy as np


def main():
    a = np.arange(1, 15)    # (14, )
    out = np.split(a, (2, 6))
    print(out)


if __name__ == "__main__":
    main()
