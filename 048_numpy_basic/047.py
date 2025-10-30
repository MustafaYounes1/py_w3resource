"""

Write a NumPy program to generate a uniform, non-uniform random sample (5 items) from a given 1-D array with and without replacement.

seed: 0x334e44660545dba1cf3d6fd46941b63
population: [0 1 2 3 4 5 6 7 8 9]

uniform sampling:
    a sample of 7 items without replacement:    [3 4 0 5 7 1 9]
    a sample of 7 items with replacement:       [1 5 6 8 8 9 3]

non-uniform sampling:
    sampling probability of each item: [0.0 0.0 0.0 0.0 0.0 0.5 0.0 0.0 0.5 0.0]
    a sample of 2 items without replacement:    [8 5]
    a sample of 7 items with replacement:       [5 5 5 5 5 5 8]

"""

import numpy as np


def main():
    rng = np.random.default_rng(0x334e44660545dba1cf3d6fd46941b63)
    print(np.arange(10))
    # uniform sampling
    print(f"uniform sampling (without replacement):     {rng.choice(10, size=7, replace=False)}")
    print(f"uniform sampling (with replacement):        {rng.choice(10, size=7, replace=True)}")

    # non-uniform sampling
    p = np.r_[[0] * 5, 0.5, 0, 0, 0.5, 0]       # non-uniform sampling (would only choose 5/8)
    print(f"non-uniform sampling (without replacement): {rng.choice(10, p=p, size=2, replace=False)}")
    print(f"non-uniform sampling (with replacement):    {rng.choice(10, p=p, size=7, replace=True)}")


if __name__ == "__main__":
    main()
