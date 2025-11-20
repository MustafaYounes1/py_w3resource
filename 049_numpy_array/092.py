"""

Write a NumPy program to get the magnitude of a vector in NumPy.

array([1, 2, 3, 4, 5])  ->  7.416198487095663

"""

import numpy as np


def main():
    vec = np.array([1, 2, 3, 4, 5])
    print(np.linalg.norm(vec))


if __name__ == "__main__":
    main()
