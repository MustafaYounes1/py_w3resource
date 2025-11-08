"""

Write a NumPy program to change an array's data type.

input:      (dtype: int16)
[[ 2 4 6]
[ 6 8 10]]

output:     (dtype: float32)
[[ 2. 4. 6.]
[ 6. 8. 10.]]

"""

import numpy as np


def main():
    a = np.array([[2, 4, 6], [6, 8, 10]], dtype = np.int16)
    print(a, "\n")

    b = a.astype(np.float32, casting="safe")
    print(b)


if __name__ == "__main__":
    main()
