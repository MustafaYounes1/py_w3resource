"""

Find the mean of each row in a 3x3 random list where the number are in the range [0, 10].

"""

import random
from statistics import mean


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(3)] for __ in range(3)]
    print(f"The random list: {lst}")
    means = [mean(_) for _ in lst]
    print(f"The means: {means}")


if __name__ == "__main__":
    main()
