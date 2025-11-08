"""

Write a NumPy program to create a 2-dimensional array of size 2x3 (composed of 4-byte integer elements).
Print the shape, type and data type of the array.

shape:      (2, 3)
type:       <class 'numpy.int32'>
datatype:   int32

"""

import numpy as np


def main():
    a = np.empty((2, 3), dtype=np.int32)
    print(f"shape:      {a.shape}\n"
          f"type:       {a.dtype.type}\n"
          f"datatype:   {a.dtype}")


if __name__ == "__main__":
    main()
