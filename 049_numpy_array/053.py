"""

Write a NumPy program to convert specified inputs into arrays with at least one dimension.

1                       ->  [1]                 (1,)
[4, 5]                  ->  [4, 5]              (2,)
[[1, 2], [3, 4]]        ->  [[1, 2], [3, 4]]    (2, 2)

"""

import numpy as np


def main():
    data = [
        1,
        [4, 5],
        [[1, 2], [3, 4]]
    ]

    for _ in data:
        a = np.atleast_1d(_)
        print(a.tolist(), a.shape)


if __name__ == "__main__":
    main()
