"""

Write a NumPy program to find the real and imaginary parts of an array of complex numbers.

[1, 0.7 + 0.7j]

real part:      [1.  0.7]
imaginary part: [0.  0.7]

"""

import numpy as np


def main():
    a = np.array([1, 0.7 + 0.7j])
    print(f"real part:      {a.real}")
    print(f"imaginary part: {a.imag}")


if __name__ == "__main__":
    main()
