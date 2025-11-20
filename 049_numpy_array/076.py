"""

Write a NumPy program to create an array of (3, 4) shapes and convert the array elements into smaller chunks.

array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

chunk_1:    [0 4 8]
chunk_2:    [1 5 9]
chunk_3:    [ 2  6 10]
chunk_4:    [ 3  7 11]

"""

import numpy as np


def main():
    a = np.arange(12).reshape(3, 4)

    for chunk in np.nditer(a, order='F', flags=["external_loop"]):
        print(chunk)


if __name__ == "__main__":
    main()
