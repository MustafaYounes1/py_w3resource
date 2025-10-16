"""

Write a NumPy program to generate a random number uniformly distributed over the range [0, 1).

Note: For reproducibility, use the following seed: '0x22ca5f1939e020a9b9af01ce3d98b7fa'

-> 0.4191924645728484

"""

import numpy as np


def main():
    rng = np.random.default_rng(0x22ca5f1939e020a9b9af01ce3d98b7fa)
    print(rng.random())


if __name__ == "__main__":
    main()
