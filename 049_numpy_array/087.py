"""

Write a NumPy program to replace all elements of NumPy array that are greater than the specified array.

Original array:
array([[0.42436315, 0.48558583, 0.32924763],
       [0.7439979 , 0.58220701, 0.38213418],
       [0.5097581 , 0.34528799, 0.1563123 ]])

Replace all elements of the said array with 0.5 which are greater than 0.5
[[0.42436315 0.48558583 0.32924763]
 [0.5        0.5        0.38213418]
 [0.5        0.34528799 0.1563123 ]]

"""

import numpy as np


def main():
    a = np.array([[0.42436315, 0.48558583, 0.32924763],
                  [0.7439979 , 0.58220701, 0.38213418],
                  [0.5097581 , 0.34528799, 0.1563123 ]])
    a[a > 0.5] = 0.5
    print(a)


if __name__ == "__main__":
    main()
