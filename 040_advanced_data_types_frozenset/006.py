"""

Write a Python program that uses a frozenset as a key in a dictionary.


"""

import random


def main():
    s0 = frozenset(random.randint(-10, 10) for _ in range(10))
    s1 = frozenset(random.randint(-10, 10) for _ in range(10))

    fs_2_sum: dict[frozenset[int], int] = {s: sum(s) for s in (s0, s1)}
    print(fs_2_sum)


if __name__ == "__main__":
    main()
