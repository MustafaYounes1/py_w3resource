"""

Write a NumPy program to create a two-dimensional array with shape (100, 100) of random numbers.
Select random numbers from a normal distribution (200, 7).

"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    rng = np.random.default_rng(0x334e44660545dba1cfb3d6fd46941b63)
    a = rng.normal(200, 7, size=(100, 100))
    b = rng.normal(200, 7, size=(100, 100))

    plt.hist([a.flat, b.flat], bins="auto", density=True, color=["green", "orange"], alpha=0.6, label=['a', 'b'])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
