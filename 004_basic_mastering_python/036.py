"""

Create a 3x3 list with random values ranging in [0, 10] and sort each row.

"""

import random


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(3)] for __ in range(3)]
    print(lst)
    print(
        [sorted(_) for _ in lst]
    )


if __name__ == "__main__":
    main()
