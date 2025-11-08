"""

Write a NumPy program to create a new array of 3*5, filled with 2.

Expected Output:

[[2 2 2 2 2]
 [2 2 2 2 2]
 [2 2 2 2 2]]

"""

import numpy as np


def main():
    a = np.full((3, 5), fill_value=2)
    print(a)


if __name__ == "__main__":
    main()
