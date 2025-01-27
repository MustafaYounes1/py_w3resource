"""

Write a Python program to filter a list of integers using Lambda.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Even numbers from the said list:
[2, 4, 6, 8, 10]

Odd numbers from the said list:
[1, 3, 5, 7, 9]

"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(filter(lambda _: _ % 2 == 0, lst)))
    print(list(filter(lambda _: _ % 2 != 0, lst)))


if __name__ == "__main__":
    main()
