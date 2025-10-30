"""

Write a NumPy program to convert an array to a floating type.

[1, 2, 3, 4] -> [1. 2. 3. 4.]

"""

import numpy as np


def main():
    a = np.asarray([1, 2, 3, 4], dtype=np.float64)
    print(a)


if __name__ == "__main__":
    main()
