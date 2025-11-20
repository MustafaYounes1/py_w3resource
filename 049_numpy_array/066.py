"""

Write a NumPy program to make an array immutable (read-only).

"""

import numpy as np


def main():
    a = np.empty(10)
    a.flags.writeable = False

    try:
        a[0] = 0

    except ValueError:
        print("The array is read-only")

    else:
        print("The array was updated successfully")


if __name__ == "__main__":
    main()
