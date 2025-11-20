"""

Write a NumPy program to convert raw array data to a binary string and create the array back from the binary string.

input:  np.arange(5, dtype=np.uint8)

b'\x00\x01\x02\x03\x04'
[0 1 2 3 4]

"""

import numpy as np


def main():
    a = np.arange(5, dtype=np.uint8)
    b = a.tobytes()
    print(b)
    c = np.frombuffer(b, dtype=np.uint8)
    print(c)


if __name__ == "__main__":
    main()
