"""

Write a NumPy program to save a random 6x4 float32 array (values are in [-5, 5)) to a text file and load it.

"""

import numpy as np


def main():
    rng = np.random.default_rng(0xf0abae5c1d9d4e27fec66d4029220f79)

    # `.random` by default gives values in [0, 1) -> scale and shift the range to [-5, 5)
    a = 10 * rng.random(size=(6, 4), dtype=np.float32) - 5

    file_name = "036_6x4_float32.txt"
    header = "{:^12s}|{:^12s}|{:^12s}|{:^12s}".format("col1", "col2", "col3", "col4")
    np.savetxt(file_name, a, fmt="%+12.8f", header=header)

    b = np.loadtxt(file_name, skiprows=1, dtype=a.dtype, ndmin=a.ndim)  # skip the header
    assert a.dtype == b.dtype and np.allclose(a, b), "Loaded array is not close to the original array"


if __name__ == "__main__":
    main()
