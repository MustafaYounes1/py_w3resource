"""

Write a NumPy program to print the full NumPy array, without truncation.

Note: By default, NumPy triggers summarization when the size of the array is greater than or equal to 1000

"""

import numpy as np
import sys


def main():
    a = np.arange(1001)
    print(a)    # triggers summarization

    # suppress the summarization
    with np.printoptions(threshold=sys.maxsize):
        print(a)

if __name__ == "__main__":
    main()
