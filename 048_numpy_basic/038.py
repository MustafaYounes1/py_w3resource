"""

Write a NumPy program to convert a given list into an array, then again convert it into a list.

Check initial list and final list are equal or not.

Input list:     [[1, 2], [3, 4], [5, 6]]

"""

import numpy as np


def main():
    lst = [[1, 2], [3, 4], [5, 6]]
    a = np.array(lst)
    assert a.tolist() == lst, "roundtrip conversion failed"


if __name__ == "__main__":
    main()
