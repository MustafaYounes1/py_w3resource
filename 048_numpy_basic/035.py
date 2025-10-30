"""

Write a NumPy program to save two random arrays (3x3 ints in the range [-4, 5), 5x4 floats in the range [-2, 2)) to
a binary file and reload them.

"""

import numpy as np


def main():
    rng = np.random.default_rng(0xf0abae5c1d9d4e27fec66d4029220f79)

    ints = rng.integers(-4, 5, size=(3, 3))
    floats = rng.uniform(-2, 2, size=(5, 4))

    print(ints)
    print(floats)

    file_name = "035_3x3_int8_5x4_float64.npz"

    # save several arrays into a single file in 'compressed' `.npz` format.
    # you can also use `savez` to save several arrays into a single file in 'uncompressed' `.npz` format.
    np.savez_compressed(file_name, ints=ints, floats=floats)

    # reload them into a dictionary-like `NpzFile`
    loaded = np.load(file_name)
    print(loaded.files)         # query for the NpzFile's list of arrays

    l_ints, l_floats = loaded["ints"], loaded["floats"]
    assert l_ints.dtype == ints.dtype and np.array_equal(loaded["ints"], ints), f"Loaded ints are not identical to the int array"
    assert l_ints.dtype == ints.dtype and np.allclose(loaded["floats"], floats), f"Loaded floats are not identical to the float array"


if __name__ == "__main__":
    main()
