"""

Write a NumPy program to sort a given array by row and column in ascending order.

array([[22, 15, 14, 16,  9, 18],
       [ 3, 20, 11, 17, 23,  6],
       [21,  5, 12,  0,  8, 19],
       [ 1, 13, 10,  2,  7,  4]])

sorted by row:
[[ 9 14 15 16 18 22]
 [ 3  6 11 17 20 23]
 [ 0  5  8 12 19 21]
 [ 1  2  4  7 10 13]]

sorted by column:
[[ 1  5 10  0  7  4]
 [ 3 13 11  2  8  6]
 [21 15 12 16  9 18]
 [22 20 14 17 23 19]]

"""

import numpy as np


def main():
    a = np.array([[22, 15, 14, 16,  9, 18],
                  [ 3, 20, 11, 17, 23,  6],
                  [21,  5, 12,  0,  8, 19],
                  [ 1, 13, 10,  2,  7,  4]])

    print("sorted by row:")
    print(np.sort(a, axis=-1), "\n")

    print("sorted by column:")
    print(np.sort(a, axis=0), "\n")



if __name__ == "__main__":
    main()
