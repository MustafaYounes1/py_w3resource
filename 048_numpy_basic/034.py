"""

Write a NumPy program to save a random 3x3 integer array to a binary file and reload it.

"""

import numpy as np


def main():
    rng = np.random.default_rng(0xf0abae5c1d9d4e27fec66d4029220f79)
    a = rng.integers(-128, 127, endpoint=True, size=(3, 3))
    print(a)

    # save the array to a '.npy' binary file
    file_name = "034_random_3x3_int8.npy"
    np.save(file_name, a)

    # reload it
    b = np.load(file_name)
    assert a.dtype == b.dtype and np.array_equal(a, b), "Loaded array isn't identical to the saved array."


if __name__ == "__main__":
    main()
