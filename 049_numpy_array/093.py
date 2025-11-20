"""

Write a NumPy program to count the frequency of distinct values in a NumPy array.

input:  array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])

items: [10 20 30 40 50]
frequencies: [3 4 2 2 1]

"""

import numpy as np


def main():
    a = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
    items, counts = np.unique(a, return_counts=True)
    print(f"items: {items}\nfrequencies: {counts}")


if __name__ == "__main__":
    main()
