"""

Create a 3x3 list with random integers in [0, 10] and replace all values greater than 5 with that 5.

"""

import random


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(3)] for __ in range(3)]
    print(lst)
    print(
        [[5 if _ > 5 else _ for _ in row] for row in lst]
    )


if __name__ == "__main__":
    main()
