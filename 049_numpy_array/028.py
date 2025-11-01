"""

Write a NumPy program to sort along the first and last axes of an array.

[[4 6]
 [2 1]]

sorted along rows:
[[4 6]
 [1 2]]

sorted along columns:
[[2 1]
 [4 6]]

"""

import numpy as np


def main():
    a = np.array([[4, 6], [2, 1]])
    print(a)
    print(f"sorted along rows:          \n{np.sort(a, axis=-1)}")
    print(f"sorted along columns:       \n{np.sort(a, axis=0)}")


if __name__ == "__main__":
    main()
