"""

Write a Python program to find the characters in a list of strings that occur more than a given number.
Note: take into consideration all occurrences of a character in all strings

['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd'], 3   =>  ['a', 'd', 'f', 's']

"""

from collections import Counter


def main():
    lst, count = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd'], 3
    c = Counter("".join(lst))
    print(list(filter(lambda _: c[_] > count, c)))


if __name__ == "__main__":
    main()
