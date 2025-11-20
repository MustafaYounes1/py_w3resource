"""

Write a NumPy program to convert a NumPy array into a Python list structure.

array([[0, 1],
       [2, 3],
       [4, 5]])

output:     [[0, 1], [2, 3], [4, 5]]

"""

import numpy as np


def main():
    a = np.arange(6).reshape(3, 2)
    print(a.tolist())


if __name__ == "__main__":
    main()
