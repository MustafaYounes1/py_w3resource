"""

Write a Python program to get unique values from a list.

[10, 20, 30, 40, 20, 50, 60, 40]    =>  {40, 10, 50, 20, 60, 30}

"""


def main():
    lst = [10, 20, 30, 40, 20, 50, 60, 40]
    print(set(lst))


if __name__ == "__main__":
    main()
