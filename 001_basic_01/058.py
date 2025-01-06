"""

Write a Python program to sum the first n positive integers.

"""


def main():
    n = int(input("Enter the positive integer n: "))
    print(sum(list([_ for _ in range(1, n + 1)])))
    # or alternatively: (n * (n + 1)) / 2


if __name__ == "__main__":
    main()
