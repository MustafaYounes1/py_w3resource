"""

Write a NumPy program to generate a generic 4x4 Gaussian-like array (standard gaussian).

seed: 0xb3519b5db0e0977bad126321e9f696c8

[[ 0.49737208 -0.23908141  2.14912623 -0.59887919]
 [-0.09298079 -0.46453962  0.79208988 -1.1476293 ]
 [-0.23561516 -1.77613102  0.95333392 -0.05360484]
 [ 0.14675301  1.48791039 -0.08386625  1.08575884]]

"""

import numpy as np


def main():
    rng = np.random.default_rng(0xb3519b5db0e0977bad126321e9f696c8)
    a = rng.normal(size=(4, 4))
    print(a)


if __name__ == "__main__":
    main()
