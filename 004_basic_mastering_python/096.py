"""

Find the first non-repeated character in a string.

swiss   =>  w

"""


def main():
    s = "swiss"
    print(list(filter(lambda x: s.count(x) == 1, s))[0])


if __name__ == "__main__":
    main()
