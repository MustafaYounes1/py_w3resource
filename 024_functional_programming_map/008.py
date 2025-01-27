"""

Write a Python program to convert a given list of integer to list of strings.

[1, 2, 3, 4]    =>  ['1', '2', '3', '4']

"""


def main():
    lst = [1, 2, 3, 4]
    print(list(map(str, lst)))


if __name__ == "__main__":
    main()
