"""

Write a Python program to count the frequency of values in a dictionary.

{'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

{10: 2, 40: 2, 20: 2, 70: 1, 80: 1}

"""

from collections import Counter


def main():
    d = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
    print(dict(Counter(d.values())))


if __name__ == "__main__":
    main()
