"""

Write a Python program to create a list by concatenating a given list with a range from 1 to n.

['p', 'q'], 5

['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

"""

from itertools import chain


def main():
    lst = ['p', 'q']
    n = 5
    print(
        list(
            chain.from_iterable(
                [[f"{__}{_}" for __ in lst] for _ in range(1, n + 1)]
            )
        )
    )


if __name__ == "__main__":
    main()
