"""

Write a Python program to check if a given value is present in a set or not.

{1, 3, 5, 7, 9, 11}

6   =>  False
7   =>  True
11  =>  True
0   =>  False

"""


def main():
    s = {1, 3, 5, 7, 9, 11}
    items = 6, 7, 11, 0

    for i in items:
        print(i in s)


if __name__ == "__main__":
    main()
