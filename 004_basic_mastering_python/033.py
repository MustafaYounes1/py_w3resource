"""

Calculate the mean of each column in a 3x3 random list where the values range in [0, 10].

"""

import random
from statistics import mean


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(3)] for __ in range(3)]
    print(f"The random list: {lst}")
    print(
        [mean([lst[i][j] for i in range(3)]) for j in range(3)]
    )


if __name__ == "__main__":
    main()
