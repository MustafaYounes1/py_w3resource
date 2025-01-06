"""

Compute the cumulative sum of elements along the third row and column in a random 4x4 list where the number range in
[0, 10].

"""

import random


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(4)] for __ in range(4)]
    print(lst)
    print(f"Sum of third row: {sum(lst[2][:])}")
    print(f"Sum of third column: {sum([lst[i][2] for i in range(4)])}")


if __name__ == "__main__":
    main()
