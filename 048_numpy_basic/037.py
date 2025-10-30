"""

Write a NumPy program to convert a 2x2 random int8 array into bytes, and load it as an array.

"""

import numpy as np


def main():
    rng = np.random.default_rng(0xf0abae5c1d9d4e27fec66d4029220f79)
    a = rng.integers(-128, 127, endpoint=True, size=(2, 2))

    print(a)
    buffer = a.tobytes()
    print(buffer)

    b = np.frombuffer(buffer, dtype=a.dtype).reshape(a.shape)
    assert a.dtype == b.dtype and np.array_equal(a, b), "Loaded array isn't identical to the original array"


if __name__ == "__main__":
    main()
