"""

Write a NumPy program to create the following arrays:

a:  [0 1 2 3 4 5 6 7 8 9]
b:  [10 30 50 70 90]
c   [ 100  200  300  400  500  600  700  800  900 1000]

"""

import numpy as np


def main():
    a = np.arange(10)
    b = np.arange(10, 101, 20)
    c = np.arange(100, 1001, 100)

    print(f"a:  {a}")
    print(f"b:  {b}")
    print(f"c   {c}")


if __name__ == "__main__":
    main()
