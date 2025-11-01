"""

Write a NumPy program to save a NumPy array to a text file.

see: "031.txt" (a similar output file is expected)

"""

import numpy as np


def main():
    a = np.arange(10*10).reshape(10, 10)
    np.savetxt("031.txt", a, delimiter="|", fmt="%2d", header="(10, 10) int Array", footer="End of Array")
    b = np.loadtxt("031.txt", dtype=int, ndmin=2, delimiter="|")
    assert b.dtype == a.dtype and np.array_equal(a, b), "loaded array isn't identical to the original array"

if __name__ == "__main__":
    main()
