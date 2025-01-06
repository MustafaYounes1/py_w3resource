"""

Create a 3x3 random list where the number range in [0, 10] and normalize each column by its range (MinMax).
    x' = (x - min) / (max - min)

"""

import random


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(3)] for __ in range(3)]
    print(lst)
    for j in range(3):
        c = [lst[i][j] for i in range(3)]
        for i in range(3):
            lst[i][j] = (lst[i][j] - min(c)) / (max(c) - min(c))

    print(lst)


if __name__ == "__main__":
    main()
