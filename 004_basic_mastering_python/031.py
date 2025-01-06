"""

Create a random 3x3 list of lists and replace all values greater than 0.5 with 1 and all others with 0.

"""

import random


def main():
    random.seed(0)
    lst = [[random.random() for __ in range(3)] for _ in range(3)]
    print(lst)
    print(
        [[1 if _ > 0.5 else 0 for _ in row] for row in lst]
    )


if __name__ == "__main__":
    main()
