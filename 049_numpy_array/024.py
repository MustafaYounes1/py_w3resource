"""

Write a NumPy program to construct an array by repeating.

[1, 2, 3, 4]

    Repeating 2 times
    [1 2 3 4 1 2 3 4]

    Repeating 3 times
    [1 2 3 4 1 2 3 4 1 2 3 4]

[[1 2]
 [3 4]]

    repeat the array two times vertically:
    [[1 2]
     [3 4]
     [1 2]
     [3 4]]

    repeat the array two times horizontally:
    [[1 2 1 2]
     [3 4 3 4]]

    repeat the array two times vertically/horizontally:
    [[1 2 1 2]
     [3 4 3 4]
     [1 2 1 2]
     [3 4 3 4]]

"""

import numpy as np


def main():
    a = np.arange(1, 5)
    print(a)
    print(f"repeat the entire array 2 times:        {np.tile(a, 2)}")
    print(f"repeat the entire array 3 times:        {np.tile(a, 3)}", "\n")

    b = np.array([[1, 2], [3, 4]])
    print(b)
    print(f"repeat the array two times vertically:                  \n{np.tile(b, (2, 1))}")
    print(f"repeat the array two times horizontally:                \n{np.tile(b, (1, 2))}")
    print(f"repeat the array two times vertically/horizontally:     \n{np.tile(b, (2, 2))}")

if __name__ == "__main__":
    main()
