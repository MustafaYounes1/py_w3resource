"""

Write a NumPy program to convert (in sequence depth wise (along the third axis)) two 1-D arrays into a 3-D array.

input 1: [10 20 30]
input 2: [40 50 60]

output:         (shape (1, 3, 2))
[[[10 40]
  [20 50]
  [30 60]]]

"""

import numpy as np


def main():
    a, b = np.arange(10, 40, 10), np.arange(40, 70, 10)  # each of shape (3,)
    print(a)
    print(b, "\n")

    c = np.dstack((a, b))                               # (1, 3, 2)
    print(c)


if __name__ == "__main__":
    main()
