"""

Write a Python program to remove duplicates from a list.

[10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]    =>  [40, 10, 80, 50, 20, 60, 30]

"""


def main():
    lst = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    print(list(set(lst)))


if __name__ == "__main__":
    main()
