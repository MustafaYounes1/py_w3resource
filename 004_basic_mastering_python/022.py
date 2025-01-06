"""

Create a random 4x4 list of lists where the values are in the range [0, 10] and extract the diagonal elements.

"""

import random


def main():
    random.seed(0)

    lst = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
    print(f"The random list: {lst}")
    d = [lst[i][j] for i in range(len(lst)) for j in range(len(lst[i])) if i == j]
    print(f"The diagonal elements are: {d}")


if __name__ == "__main__":
    main()
