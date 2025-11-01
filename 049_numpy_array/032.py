"""

Write a NumPy program to find the memory size of a NumPy array.

np.zeros((4, 4), dtype=np.int8) ->  16

"""

import numpy as np


def main():
    a = np.zeros((4, 4), dtype=np.int8)
    print(a.nbytes)


if __name__ == "__main__":
    main()
