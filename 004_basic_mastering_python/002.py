"""

Convert a list of integers to a list of strings.

e.g. lst = [1, 2, 3, 4, 5]      =>       ['1', '2', '3', '4', '5']

"""


def main():
    lst = [1, 2, 3, 4, 5]
    print(list(map(str, lst)))


if __name__ == "__main__":
    main()
