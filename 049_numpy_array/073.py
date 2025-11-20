"""

Write a NumPy program to combine a one and two dimensional array together and display their elements.

One dimensional array:
[0 1 2 3]

Two dimensional array:
[[0 1 2 3]
[4 5 6 7]]

0:0
1:1
2:2
3:3
0:4
1:5
2:6
3:7

"""

import numpy as np


def main():
    a = np.arange(4)
    b = np.arange(8).reshape(2, 4)

    for aa, bb in np.broadcast(a, b):
        print(f"{aa}:{bb}")


if __name__ == "__main__":
    main()
