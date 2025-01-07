"""

Write a Python program to create and display all combinations of letters, selecting each letter from a different key
in a dictionary.

{'1':['a','b'], '2':['c','d']}

ac
ad
bc
bd

"""

from itertools import product


def main():
    data = {'1': ['a', 'b'], '2': ['c', 'd']}
    for comb in product(*[data[k] for k in sorted(data)]):
        print("".join(comb))


if __name__ == "__main__":
    main()
