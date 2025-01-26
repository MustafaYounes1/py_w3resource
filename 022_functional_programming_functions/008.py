"""

Write a Python function that takes a list and returns a new list with distinct elements from the first list.

[1, 2, 3, 3, 3, 3, 4, 5]  => [1, 2, 3, 4, 5]

"""


def uniquify(lst: list[...]) -> list[...]:
    return list(set(lst))


def main():
    print(uniquify([1, 2, 3, 3, 3, 3, 4, 5]))


if __name__ == "__main__":
    main()
