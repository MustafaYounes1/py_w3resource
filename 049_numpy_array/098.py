"""

Write a NumPy program to take values from a source array and put them at specified indices of another array.

array([10., 10., 20., 30., 30.])

Put 0 and 40 in first and fifth position of the above array

-> [ 0. 10. 20. 30. 40.]

"""

import numpy as np


def main():
    a = np.array([10., 10., 20., 30., 30.])
    np.put(a, [0, 4], [0, 40])
    print(a)


if __name__ == "__main__":
    main()
