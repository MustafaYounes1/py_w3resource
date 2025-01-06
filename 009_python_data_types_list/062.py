"""

Write a Python program to print a list of space-separated elements.

num = [1, 2, 3, 4, 5]

1 2 3 4 5

"""


def main():
    num = [1, 2, 3, 4, 5]
    print(" ".join(list(map(str, num))))


if __name__ == "__main__":
    main()
