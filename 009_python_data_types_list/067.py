"""

Write a Python program to check if all values in a list that are greater than or equal to a specified number.

[220, 330, 500], 200    =>  True
[12, 17, 21], 25        =>  False

"""


def main():
    lst, v = [12, 17, 21], 25
    print(all(_ >= v for _ in lst))


if __name__ == "__main__":
    main()
