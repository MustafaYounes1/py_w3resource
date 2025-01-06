"""

Swap the first and third rows in a 4x4 list of random values ranging in [0, 10]

"""

import random


def main():
    random.seed(0)
    lst = [[random.randint(0, 10) for _ in range(4)] for __ in range(4)]
    print(f"The random list: {lst}")
    lst[0], lst[2] = lst[2], lst[0]
    print(f"After the swap: {lst}")


if __name__ == "__main__":
    main()
