"""

Count the number of elements in a list within a specific range.

lst = [2, 5, 8, 10, 12, 15]
range:  [5, 12]

output: 4

"""


def main():
    lst = [2, 5, 8, 10, 12, 15]
    r = range(5, 13)
    print(len([_ for _ in lst if _ in r]))


if __name__ == "__main__":
    main()
