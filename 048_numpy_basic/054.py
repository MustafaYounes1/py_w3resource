"""

Write a NumPy program to create a three-dimensional array with the shape (3,5,4) and set it to a variable.

[[[5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]]

 [[5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]]

 [[5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]
  [5 5 5 5]]]

"""

import numpy as np


def main():
    a = np.empty((3,5,4), dtype=int)
    a.fill(5)
    print(a)


if __name__ == "__main__":
    main()
