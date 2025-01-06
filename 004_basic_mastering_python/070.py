"""

Count the occurrences of each character in a string.

e.g.    hello   =>  [('h', 1), ('e', 1), ('l', 2), ('o', 1)]
"""

from collections import Counter


def main():
    s = "hello"
    print(list(Counter(s).items()))


if __name__ == "__main__":
    main()
