"""

Write a NumPy program to convert a list and tuple into arrays.

[1, 2, 3, 4, 5, 6, 7, 8]

    [1 2 3 4 5 6 7 8]

([8, 4, 6], [1, 2, 3])

    [[8 4 6]
     [1 2 3]]

"""

import numpy as np


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    print(np.array(lst))

    tup = ([8, 4, 6], [1, 2, 3])
    print(np.array(tup))


if __name__ == "__main__":
    main()
