"""

Write a NumPy program to create an empty int8 array of shape (2, 2), and a float32 array of shape (3, 4) full of 5s.

"""

import numpy as np


def main():
    i8 = np.empty((2, 2), dtype=np.int8)
    print(i8, "\n")

    f32 = np.full((2, 2), fill_value=5, dtype=np.float32)
    print(f32)


if __name__ == "__main__":
    main()
