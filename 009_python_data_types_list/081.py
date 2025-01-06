"""

Write a Python program to extract a given number of randomly selected elements from a given list.

[1, 1, 2, 3, 4, 4, 5, 1], 3

[4, 4, 1]

"""

import random


def main():
    random.seed(0)
    lst, n = [1, 1, 2, 3, 4, 4, 5, 1], 3
    print(random.sample(lst, k=3))


if __name__ == "__main__":
    main()
