"""

Write a Python function to create and print a list where the values are the squares of numbers between 1 and 20
(both included).

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

"""


def get_squares(s: int = 1, e: int = 20) -> list[int]:
    return list(map(lambda _: pow(_, 2), range(s, e + 1)))


def main():
    print(get_squares())


if __name__ == "__main__":
    main()
