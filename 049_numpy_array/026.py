"""

Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array.

[1 2 3 4 5 6]

    max index:     5
    min index:     0

[[-1  2  0]
 [-2  0  3]]

    max index along rows:         [1 2]
    min index along rows:         [0 0]
    max index along columns:      [0 0 1]
    min index along columns:      [1 1 0]

"""

import numpy as np


def main():
    a = np.arange(1, 7)
    print(a)
    print(f"max index:     {a.argmax()}")
    print(f"min index:     {a.argmin()}")

    b = np.array([[-1, 2, 0], [-2, 0, 3]])
    print(b)
    print(f"max index along rows:         {b.argmax(axis=1)}")
    print(f"min index along rows:         {b.argmin(axis=1)}")
    print(f"max index along columns:      {b.argmax(axis=0)}")
    print(f"min index along columns:      {b.argmin(axis=0)}")


if __name__ == "__main__":
    main()
