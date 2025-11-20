"""

Write a NumPy program to select indices satisfying multiple conditions in a NumPy array.

a = np.array([97, 101, 105, 111, 117])
b = np.array(['a', 'e', 'i', 'o', 'u'])

Select the elements from the second array corresponding to elements in the first array that are greater than 100 and
less than 110

-> ['e' 'i']

"""

import numpy as np


def main():
    a = np.array([97, 101, 105, 111, 117])
    b = np.array(['a', 'e', 'i', 'o', 'u'])
    print(b[(a > 100) & (a < 110)])


if __name__ == "__main__":
    main()
