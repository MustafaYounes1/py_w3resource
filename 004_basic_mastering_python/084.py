"""

Find the sum of the digits of a number.

12345   =>  15

"""


def main():
    n = 12345
    print(sum(list(map(int, str(n)))))


if __name__ == "__main__":
    main()
