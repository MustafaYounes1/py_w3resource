"""

Write a NumPy program to view inputs as arrays with at least two/three dimensions

1
    2d: [[1]]                           (1, 1)
    3d: [[[1]]]                         (1, 1, 1)

[4, 5]
    2d: [[4, 5]]                        (1, 2)
    3d: [[[4], [5]]]                    (1, 2, 1)

[[1, 2], [3, 4]]
    2d: [[1, 2], [3, 4]]                (2, 2)
    3d: [[[1], [2]], [[3], [4]]]        (2, 2, 1)

"""

import numpy as np


def main():
    data = [
        1,
        [4, 5],
        [[1, 2], [3, 4]]
    ]

    for _ in data:
        dd, ddd = np.atleast_2d(_), np.atleast_3d(_)
        print(dd.tolist(), dd.shape)
        print(ddd.tolist(), ddd.shape)


if __name__ == "__main__":
    main()
