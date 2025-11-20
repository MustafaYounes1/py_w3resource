"""

Write a NumPy program to convert a NumPy array into a CSV file.

see: `100.csv`

"""

import numpy as np


def main():
    a = np.arange(24).reshape(4, 6)
    np.savetxt('100.csv', a, delimiter=',', fmt="%2d", comments='', header='col1 , col2 , col3 , col4 , col5 , col6')


if __name__ == "__main__":
    main()
