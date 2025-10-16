"""

Write a NumPy program to test elements-wise for positive or negative infinity.

np.array([-np.inf, 1, 0, np.nan, np.inf])       ; inf/-inf      ->  [ True False False False  True]
                                                ; inf           ->  [False False False False  True]
                                                ; -inf          ->  [ True False False False False]

"""

import numpy as np


def main():
    a = np.array([-np.inf, 1, 0, np.nan, np.inf])
    print(f"inf/-inf:   {np.isinf(a)}")
    print(f"inf:        {np.isposinf(a)}")
    print(f"-inf:       {np.isneginf(a)}")


if __name__ == "__main__":
    main()
