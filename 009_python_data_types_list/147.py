"""

Write a Python program to combine two lists into another list randomly.

[1, 2, 7, 8, 3, 7]
[4, 3, 8, 9, 4, 3, 8, 9]

[4, 1, 2, 3, 8, 9, 4, 3, 7, 8, 9, 8, 3, 7]

"""

import random


def main():
    random.seed(0)

    lst1 = [1, 2, 7, 8, 3, 7]
    lst2 = [4, 3, 8, 9, 4, 3, 8, 9]

    res = list(lst1)
    res.extend(lst2)
    random.shuffle(res)

    print(res)

if __name__ == "__main__":
    main()
