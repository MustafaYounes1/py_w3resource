"""

Write a Python function that filters out all elements less than or equal than a specified value from a list of numbers
using the filter function.

[20, 15, 24, 37, 23, 11, 7], 20     =>  [20, 15, 11, 7]

"""


def main():
    lst, n = [20, 15, 24, 37, 23, 11, 7], 20
    print(list(filter(lambda _: _ <= n, lst)))


if __name__ == "__main__":
    main()
