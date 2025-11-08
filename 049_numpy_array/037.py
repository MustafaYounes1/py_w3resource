"""

Write a NumPy program to create another shape from an array without changing its data.

input:  (shape is (3, 2))
[[1 2]
[3 4]
[5 6]]

output: (shape is (2, 3))
[[1 2 3]
[4 5 6]]

"""

import numpy as np


def main():
    a = np.arange(1, 7)
    a.shape = (3, 2)
    print(a, "\n")

    b = a.reshape(2, 3)
    assert b.base is a, f"b is expected to be a view of a"
    print(b)


if __name__ == "__main__":
    main()
