"""

Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.

Note: For reproducibility, use the following seed: '0x22ca5f1939e020a9b9af01ce3d98b7fa'

[0 4 6 6 1]

"""

import numpy as np


def main():
    rng = np.random.default_rng(0x22ca5f1939e020a9b9af01ce3d98b7fa)
    a = rng.integers(10, endpoint=True, size=5)
    print(a)


if __name__ == "__main__":
    main()
