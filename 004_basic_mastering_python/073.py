"""

Generate a list of 10 random integers in the range [0, 10].

"""

import random


def main():
    random.seed(0)
    print([random.randint(0, 10) for _ in range(10)])


if __name__ == "__main__":
    main()
