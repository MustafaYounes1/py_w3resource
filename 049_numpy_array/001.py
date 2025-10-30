"""

Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.


Original List:                  [12.23, 13.32, 100, 36.32]
One-dimensional NumPy array:    [ 12.23  13.32 100.    36.32]

"""

import numpy as np


def main():
    lst = [12.23, 13.32, 100, 36.32]
    a = np.array(lst)
    print(a)


if __name__ == "__main__":
    main()
