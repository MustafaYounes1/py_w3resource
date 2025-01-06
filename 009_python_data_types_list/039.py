"""

Write a Python program to convert a list of multiple integers into a single integer.

[11, 33, 50]    =>  113350

"""


def main():
    lst = [11, 33, 50]
    print("".join(list(map(str, lst))))


if __name__ == "__main__":
    main()
