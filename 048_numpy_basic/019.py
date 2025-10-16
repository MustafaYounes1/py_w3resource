"""

Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

[16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54]

"""

import numpy as np


def main():
    a = np.arange(15, 56)
    print(a[1:-1])


if __name__ == "__main__":
    main()
