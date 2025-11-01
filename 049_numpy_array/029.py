"""

Write a NumPy program to sort pairs of a first name and a last name and return their indices (first by last name, then by first name).

first_names = ('Shelley', 'Betsey', 'Lanell', 'Genesis', 'Margery')
last_names = ('Battle', 'Battle', 'Plotner', 'Stahl', 'Woolum')

Expected Output:
[0 1 2 3 4]

Betsey Battle
Shelley Battle
Lanell Plotner
Genesis Stahl
Margery Woolum

"""

import numpy as np


def main():
    first_names = ('Shelley', 'Betsey', 'Lanell', 'Genesis', 'Margery')
    last_names = ('Battle', 'Battle', 'Plotner', 'Stahl', 'Woolum')

    indices = np.lexsort((first_names, last_names))  # sort first along the last row, and break ties based on the first row
    print(indices)
    print("\n".join(f"{first_names[i]} {last_names[i]}" for i in indices))


if __name__ == "__main__":
    main()
