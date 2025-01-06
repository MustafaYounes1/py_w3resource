"""

Find the indices of the maximum value in each row of a 4x4 list of random values that range in [0, 10].

"""

import random


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(4)] for __ in range(3)]
    print(lst)
    print([_.index(max(_)) for _ in lst])


if __name__ == "__main__":
    main()
