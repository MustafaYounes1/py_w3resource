"""

Write a NumPy program to create a one-dimensional array of 10 pseudo-randomly generated values.
Select random numbers from a uniform distribution between 0 and 1.

[0.18138628 0.663765   0.70319871 0.20134926 0.58369598 0.81176808
 0.34364489 0.10186336 0.0698783  0.11933338]

"""

import numpy as np


def main():
    rng = np.random.default_rng(0x334e44660545dba1cfb3d6fd46941b63)
    a = rng.random(10)
    print(a)


if __name__ == "__main__":
    main()
