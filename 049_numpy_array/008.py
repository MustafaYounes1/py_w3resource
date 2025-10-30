"""

Write a NumPy program to add a custom border around an existing array.

array:
[[1 1 1]
 [1 1 1]
 [1 1 1]]

border array:
[100 100 100 100 100]

out:
[[100 100 100 100 100]
 [100   1   1   1 100]
 [100   1   1   1 100]
 [100   1   1   1 100]
 [100 100 100 100 100]]

"""

import numpy as np


def main():
    a = np.ones((3, 3), dtype=int)
    b = np.full(5, 100)
    out = np.empty_like(a, shape=np.asarray(a.shape) + 2)

    out[1:-1, 1:-1] = a
    out[[0, -1]] = b
    out[:, [0, -1]] = b[:, None]

    print(out)


if __name__ == "__main__":
    main()
