"""

Multiply all elements in a list by 2

e.g. [1, 2, 3, 4, 5]       =>      [2, 4, 6, 8, 10]

"""


def main():
    lst = [1, 2, 3, 4, 5]
    print(list(map(lambda x: x * 2, lst)))


if __name__ == "__main__":
    main()
