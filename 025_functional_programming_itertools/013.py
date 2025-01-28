"""

Write a Python program to generate all possible permutations of specified characters drawn from a specific word.
    Note: permutations with repeated chars are required

"Red"

1:  ['R', 'e', 'd']
2:  ['RR', 'Re', 'Rd', 'eR', 'ee', 'ed', 'dR', 'de', 'dd']
3:  ['RRR', 'RRe', 'RRd', 'ReR', 'Ree', 'Red', 'RdR', 'Rde', 'Rdd', 'eRR', 'eRe', 'eRd', 'eeR', 'eee', 'eed', 'edR',
    'ede', 'edd', 'dRR', 'dRe', 'dRd', 'deR', 'dee', 'ded', 'ddR', 'dde', 'ddd']

"""

from itertools import product


def main():
    print(list(map("".join, product("Red", repeat=1))))
    print(list(map("".join, product("Red", repeat=2))))
    print(list(map("".join, product("Red", repeat=3))))


if __name__ == "__main__":
    main()
