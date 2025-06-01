"""

Write a Python program that generates a frozenset containing the squares of all odd numbers from 1 to 15 using set
comprehension.

frozenset({1, 121, 225, 9, 169, 81, 49, 25})

"""


def main():
    print(frozenset({n ** 2 for n in range(1, 16) if n % 2}))


if __name__ == "__main__":
    main()
