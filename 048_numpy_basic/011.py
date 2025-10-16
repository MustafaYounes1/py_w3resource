"""

Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.

np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])

    equal:                      [ True  True  True  True  True  True  True  True  True False]
    equal with a tolerance:     [ True  True  True  True  True  True  True  True  True  True]

Note: Use the NumPy default settings for the absolute/relative tolerance values (atol=1e-08, rtol=1e-05)

"""

import numpy as np


def main():
    a = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
    b = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])     # .000001 <= 1e-08 + 1e-05 * 100.000001

    print(f"equal:                      {a == b}")              # or np.equal(a, b)
    print(f"equal with a tolerance:     {np.isclose(a, b)}")

if __name__ == "__main__":
    main()
