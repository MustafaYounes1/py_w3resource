"""

Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.

range(1, 23)    =>  [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""


def main():
    print(list(filter(lambda _: all(_ % int(__) == 0 for __ in str(_)) if "0" not in str(_) else False, range(1, 23))))


if __name__ == "__main__":
    main()
