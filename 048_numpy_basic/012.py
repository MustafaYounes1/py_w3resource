"""

Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied
by the array.

Total array size:   32 bytes  (64-bit machine)

"""

import numpy as np


def main():
    a = np.array([1, 7, 13, 105])  # default dtype is np.int64 on 64-bit machines, np.int32 on 32-bit machines
    print(f"Item size:          {a.itemsize} bytes")
    print(f"Total array size:   {a.nbytes:,} bytes")


if __name__ == "__main__":
    main()
