"""

Write a Python program to scramble the letters of a string in a given list.

['Python', 'list', 'exercises', 'practice', 'solution']
['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']

"""

import random


def main():
    random.seed(0)
    lst = ['Python', 'list', 'exercises', 'practice', 'solution']
    res = []

    for _ in lst:
        w = list(_)
        random.shuffle(w)
        res.append("".join(w))

    print(res)


if __name__ == "__main__":
    main()
