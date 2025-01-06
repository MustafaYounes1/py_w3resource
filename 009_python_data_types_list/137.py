"""

Write a Python program to find the first even and odd number in a given list of numbers.

[1, 3, 5, 7, 4, 1, 6, 8]

(4, 1)

"""


def main():
    lst = [1, 3, 5, 7, 4, 1, 6, 8]
    evens_gen = (_ for _ in lst if _ % 2 == 0)
    odds_gen = (_ for _ in lst if _ % 2 != 0)
    print((next(evens_gen), next(odds_gen)))


if __name__ == "__main__":
    main()
