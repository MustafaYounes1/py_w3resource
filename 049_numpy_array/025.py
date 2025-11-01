"""

Write a NumPy program to repeat array elements.

[1, 2, 3, 4]

    Repeating 2 times
    [1 1 2 2 3 3 4 4]

    Repeating 3 times
    [1 2 3 4 1 2 3 4 1 2 3 4]

[[0 1]
 [2 3]]

    repeat the first row once and the second twice:
    [[0 1]
     [2 3]
     [2 3]]

    repeat the first column twice and the second once:
    [[0 0 1]
     [2 2 3]]

"""

import numpy as np


def main():
    a = np.arange(1, 5)
    print(a)
    print(f"repeat elements 2 times: {np.repeat(a, 2)}")
    print(f"repeat elements 3 times: {np.repeat(a, 3)}", "\n")

    b = np.arange(4).reshape(2, 2)
    print(b)
    print(f"repeat the first row once and the second twice:     \n{np.repeat(b, [1, 2], axis=0)}")
    print(f"repeat the first column twice and the second once:  \n{np.repeat(b, [2, 1], axis=1)}")

if __name__ == "__main__":
    main()
