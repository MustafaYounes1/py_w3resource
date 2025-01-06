"""

Write a Python program to print the numbers of a specified list after removing even numbers from it.

[7, 8, 120, 25, 44, 20, 27]     =>  [7, 25, 27]

"""


def main():
    lst = [7, 8, 120, 25, 44, 20, 27]
    print(list(filter(lambda _: _ % 2 != 0, lst)))


if __name__ == "__main__":
    main()
