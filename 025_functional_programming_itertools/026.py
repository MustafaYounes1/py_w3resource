"""

Create a Python program that chooses a specified number of colors from three different colors and generates
unique combinations.

['Red', 'Green', 'Blue']

n = 1       =>  ['Red', 'Green', 'Blue']
n = 2       =>  ['Red and Green', 'Red and Blue', 'Green and Blue']
n = 3       =>  ['Red and Green and Blue']

"""

from itertools import combinations


def main():
    lst = ['Red', 'Green', 'Blue']

    print(list(map(" and ".join, combinations(lst, 1))))
    print(list(map(" and ".join, combinations(lst, 2))))
    print(list(map(" and ".join, combinations(lst, 3))))


if __name__ == "__main__":
    main()
