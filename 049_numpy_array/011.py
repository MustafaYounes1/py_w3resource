"""

Write a NumPy program to append values to the end of an array.

Original array:
[10, 20, 30]

After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]

"""

import numpy as np


def main():
    a = [10, 20, 30]
    vals = np.arange(40, 100, 10)
    print(np.append(a, vals))


if __name__ == "__main__":
    main()
