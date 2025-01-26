"""

Write a Python program to print the even numbers from a given list.

[1, 2, 3, 4, 5, 6, 7, 8, 9]   =>  [2, 4, 6, 8]

"""


def get_evens(lst: list[int]) -> list[int]:
    return list(filter(lambda _: _ % 2 == 0, lst))


def main():
    print(get_evens([1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == "__main__":
    main()
