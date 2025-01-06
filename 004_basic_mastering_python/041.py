"""

Compute the sum of diagonal elements in a 4x4 random list where the numbers are in the range [0, 10].

"""

import random


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(4)] for __ in range(4)]
    print(lst)
    print(sum([lst[i][i] for i in range(4)]))


if __name__ == "__main__":
    main()
