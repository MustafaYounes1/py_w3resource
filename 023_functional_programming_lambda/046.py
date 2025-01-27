"""

Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before
strings.

[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

"""


def main():
    lst = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
    print(sorted(lst, key=lambda _: (isinstance(_, str), _)))


if __name__ == "__main__":
    main()
