"""

Shuffle a list.

lst = [1, 2, 3, 4, 5]

"""

import random


def main():
    random.seed(0)
    lst = [1, 2, 3, 4, 5]
    random.shuffle(lst)
    print(lst)


if __name__ == "__main__":
    main()
