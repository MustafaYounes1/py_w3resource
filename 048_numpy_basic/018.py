"""

Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.

Note: For reproducibility, use the following seed: '0x22ca5f1939e020a9b9af01ce3d98b7fa'

[-0.11869655  1.69591506 -0.14144756  0.82393334 -0.25081425 -2.14130281
  0.94833402  0.67673572 -0.88364139  1.32003527 -0.17065957 -0.51081071
  0.49089871  0.55615951 -0.99268387]

"""

import numpy as np


def main():
    rng = np.random.default_rng(0x22ca5f1939e020a9b9af01ce3d98b7fa)
    a = rng.standard_normal(15)
    print(a)


if __name__ == "__main__":
    main()
