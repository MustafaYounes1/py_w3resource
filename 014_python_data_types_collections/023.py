"""

Write a Python program to get the frequency of pairs in a given list.
Note: order of elements inside the pairs shouldn't matter ([a, b] == [b, a])

[['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7']]

('4', '1') 2
('2', '7') 2
('8', '6') 2
('3', '4') 1
('8', '5') 1
('5', '7') 1

"""

from collections import Counter


def main():
    lst = [['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7']]

    # Counter works only on hashable types
    c = Counter(map(frozenset, lst))

    for pair, count in c.most_common():
        print(tuple(pair), count)


if __name__ == "__main__":
    main()
