"""

Write a NumPy program to find the number of elements in an array.
Also finds the length of one array element in bytes and the total bytes consumed by the elements.

IN8 Array, shape (2, 2)
    number of elements:     4
    item bytesize:          1
    array bytesize:         4

FLOAT16 Array, shape (3,)
    number of elements:     3
    item bytesize:          2
    array bytesize:         6

"""

import numpy as np


def inspect_arr(a: np.ndarray) -> None:
    print(f"number of elements:     {a.size}")
    print(f"item bytesize:          {a.itemsize}")
    print(f"array bytesize:         {a.nbytes}")


def main():
    a = np.empty((2, 2), dtype=np.int8)
    inspect_arr(a)
    print()

    a = np.empty(3, dtype=np.float16)
    inspect_arr(a)


if __name__ == "__main__":
    main()
