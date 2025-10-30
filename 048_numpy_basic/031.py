"""

Write a NumPy program to, given a 2d array, compute:
    * the sum of all elements,
    * the sum of each column, and
    * the sum of each row

array([[4, 3, 6, 0, 5, 4],
       [6, 2, 7, 5, 0, 4],
       [5, 9, 4, 0, 4, 3],
       [1, 1, 8, 1, 2, 8],
       [2, 8, 1, 1, 3, 3]])

sum of all elements: 110
sum of each column: [18 23 26  7 14 22]
sum of each row: [22 24 25 21 18]

"""

import numpy as np


def main():
    a = np.array([[4, 3, 6, 0, 5, 4],
                  [6, 2, 7, 5, 0, 4],
                  [5, 9, 4, 0, 4, 3],
                  [1, 1, 8, 1, 2, 8],
                  [2, 8, 1, 1, 3, 3]])

    print(f"sum of all elements: {a.sum()}")
    print(f"sum of each column:", a.sum(axis=0))
    print(f"sum of each row:", a.sum(axis=-1))


if __name__ == "__main__":
    main()
