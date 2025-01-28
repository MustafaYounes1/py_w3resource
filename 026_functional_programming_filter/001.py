"""

Write a Python function that filters out even numbers from a list of integers using the filter function.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   =>  [1, 3, 5, 7, 9]

"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(filter(lambda _: _ % 2 != 0, lst)))


if __name__ == "__main__":
    main()
