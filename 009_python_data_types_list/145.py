"""

Write a Python program to generate a number in a specified range except for some specific numbers.

Generate a number in a specified range (1, 10) except [2, 9, 10]
7

Generate a number in a specified range (-5, 5) except [-5, 0, 4, 3, 2]
-4

"""

import random


def main():
    random.seed(0)

    r1 = [_ for _ in range(1, 11) if _ not in [2, 9, 10]]
    print(random.choice(r1))

    r2 = [_ for _ in range(-5, 6) if _ not in [-5, 0, 4, 3, 2]]
    print(random.choice(r2))


if __name__ == "__main__":
    main()
