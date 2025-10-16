"""

Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given
arrays.

np.array([3, 5]), np.array([2, 5])

    greater         ->  [ True False]
    greater_equal   ->  [ True  True]

    less            ->  [False False]
    less_equal      ->  [False  True]

"""

import numpy as np


def main():
    a, b = np.array([3, 5]), np.array([2, 5])
    print(f"greater:            {a > b}")       # or np.greater(a, b)
    print(f"greater_equal:      {a >= b}")      # or np.greater_equal(a, b)
    print(f"less:               {a < b}")       # or np.less(a, b)
    print(f"less_equal:         {a <= b}")      # or np.less_equal(a, b)


if __name__ == "__main__":
    main()
