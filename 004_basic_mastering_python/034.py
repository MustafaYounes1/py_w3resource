"""

Normalize the values in each column of a 3x3 random list where the values range in [0, 10] using MinMax Scaling:
     x' = (x - min) / (max - min)

"""

import random


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(3)] for __ in range(3)]
    print(f"The random list: {lst}")

    for j in range(3):
        c = [lst[i][j] for i in range(3)]
        mi, ma = min(c), max(c)
        for i in range(3):
            lst[i][j] = (lst[i][j] - mi) / (ma - mi)

    print(lst)


if __name__ == "__main__":
    main()
