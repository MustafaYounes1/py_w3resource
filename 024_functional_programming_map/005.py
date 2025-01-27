"""

Write a Python program to square the elements of a list using the map() function.

[4, 5, 2, 9]    =>  [16, 25, 4, 81]

"""


def main():
    lst = [4, 5, 2, 9]
    print(list(map(lambda _: pow(_, 2), lst)))


if __name__ == "__main__":
    main()
