"""

Write a NumPy program to create a record array from a (flat) list of arrays.

Sample arrays: [1,2,3,4], ['Red', 'Green', 'White', 'Orange'], [12.20,15,20,40]

output:
[(1, 'Red', 12.2) (2, 'Green', 15. ) (3, 'White', 20. )
 (4, 'Orange', 40. )]

"""

import numpy as np


def main():
    lst = [[1, 2, 3, 4], ['Red', 'Green', 'White', 'Orange'], [12.20, 15, 20, 40]]
    a = np.rec.fromarrays(lst)
    print(a)


if __name__ == "__main__":
    main()
