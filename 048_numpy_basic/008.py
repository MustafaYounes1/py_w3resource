"""

Write a NumPy program to test element-wise for complex numbers, real numbers in a given array.

    np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])

        Complex mask:       [ True False False False False  True]
        Real mask:          [False  True  True  True  True False]

Also test if a given input is of an array scalar or not.

        3.1     ->  True
        [3.1]   ->  False
        []      ->  False

"""

import numpy as np


def main():
    a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
    print(f"Complex mask (a nonzero imaginary part):    {np.iscomplex(a)}")
    print(f"Complex mask (a zero imaginary part):       {np.isreal(a)}")

    for inp in [3.1, [3.1], []]:
        print(f"{inp}: {np.isscalar(inp)}")


if __name__ == "__main__":
    main()
