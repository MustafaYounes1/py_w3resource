"""

Write a Python program to read a given string character by character and compress repeated characters by storing
the length of those character(s).

AAASSSSKKIOOOORRRREEETTTTAAAABBBBBBDDDDD
[(3, 'A'), (4, 'S'), (2, 'K'), (1, 'I'), (4, 'O'), (4, 'R'), (3, 'E'), (4, 'T'), (4, 'A'), (6, 'B'), (5, 'D')]

jjjjiiiiooooosssnssiiiiwwwweeeaaaabbbddddkkkklll
[
    (4, 'j'), (4, 'i'), (5, 'o'), (3, 's'), (1, 'n'), (2, 's'), (4, 'i'), (4, 'w'), (3, 'e'), (4, 'a'), (3, 'b'),
    (4, 'd'), (4, 'k'), (3, 'l')
]

"""

from itertools import groupby


def main():
    data = ["AAASSSSKKIOOOORRRREEETTTTAAAABBBBBBDDDDD", "jjjjiiiiooooosssnssiiiiwwwweeeaaaabbbddddkkkklll"]
    for _ in data:
        print([(len(list(g)), k) for k, g in groupby(_)])


if __name__ == "__main__":
    main()
