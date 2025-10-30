"""

Write a NumPy program to create an 8x8 matrix and fill it with a checkerboard pattern.

[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]

"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.zeros((8, 8), dtype=int)
    a[::2, 1::2] = 1
    a[1::2, ::2] = 1

    print(a)

    # visualize the checkerboard
    plt.imshow(a, cmap="gray")
    plt.gca().set(xticks=(), yticks=())
    plt.show()

if __name__ == "__main__":
    main()
