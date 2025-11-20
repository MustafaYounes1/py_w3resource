"""

Write a NumPy program to create a vector of size 10 with values ranging from 0 to 1, both excluded.

[2.22507386e-308 1.00000000e-001 2.00000000e-001 3.00000000e-001
 4.00000000e-001 5.00000000e-001 6.00000000e-001 7.00000000e-001
 8.00000000e-001 9.00000000e-001]

"""

import numpy as np


def main():
    sn = np.finfo(np.float64).smallest_normal
    a = np.linspace(sn, 1, 10, endpoint=False)
    print(a)


if __name__ == "__main__":
    main()
