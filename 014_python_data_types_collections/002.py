"""

Write a Python program to find the most 3 common elements and their counts in a specified text.

lkseropewdssafsdfafkpwe

[('s', 4), ('e', 3), ('f', 3)]

"""

from collections import Counter


def main():
    s = 'lkseropewdssafsdfafkpwe'
    c = Counter(s)
    print(c.most_common(3))


if __name__ == "__main__":
    main()
