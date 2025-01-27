"""

Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]    =>  [19, 65, 57, 39, 152, 190]

"""


def main():
    lst = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
    print(list(filter(lambda _: (_ % 13 == 0) or (_ % 19 == 0), lst)))


if __name__ == "__main__":
    main()
