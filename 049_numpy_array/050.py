"""

Write a NumPy program to change two array axes.

Input:
[[1 2 3]]

output:
[[1]
[2]
[3]]

"""

import numpy as np


def main():
    a = np.array([[1, 2, 3]])
    print(a, a.shape,  "\n")

    b = a.swapaxes(0, 1)
    print(b, b.shape, "\n")


if __name__ == "__main__":
    main()
