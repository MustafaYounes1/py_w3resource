"""

Write a Python program that creates an OrderedDict and populates it with 10 random integer values as values and their
ASCII characters as keys. Print the OrderedDict.

OrderedDict(
    [('h', 104), ('K', 75), ('V', 86), ('k', 107), ('t', 116), ('G', 71), ('N', 78), ('F', 70), ('C', 67), ('I', 73)]
)


"""

from collections import OrderedDict
import random
from string import ascii_letters


def main():
    d = OrderedDict({k: ord(k) for k in random.choices(ascii_letters, k=10)})
    print(d)


if __name__ == "__main__":
    main()
