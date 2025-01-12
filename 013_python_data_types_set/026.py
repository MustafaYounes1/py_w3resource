"""

Write a Python program to find all the anagrams and group them together from a given list of strings.
Use the Python data type.

Note: two strings are considered anagrams if they have the same characters with the same frequency, but the order of
the characters is different.

['eat', 'cba', 'tae', 'abc', 'xyz']

    =>  [['eat', 'tae'], ['cba', 'abc'], ['xyz']]

['restful', 'forty five', 'evil', 'over fifty', 'vile', 'fluster']

    =>  [['restful', 'fluster'], ['forty five', 'over fifty'], ['evil', 'vile']]

"""

from collections import defaultdict


def main():
    data = [
        ['eat', 'cba', 'tae', 'abc', 'xyz'],
        [['restful', 'fluster'], ['forty five', 'over fifty'], ['evil', 'vile']]
    ]

    for lst in data:
        out = defaultdict(list)

        for _ in lst:
            out[frozenset(_)].append(_)

        print(list(out.values()))


if __name__ == "__main__":
    main()
