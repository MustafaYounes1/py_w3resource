"""

Write a Python program to check if two lists have the common elements in them in same order or not.

['red', 'green', 'black', 'orange']
['red', 'pink', 'green', 'white', 'black']
['white', 'orange', 'pink', 'black']

1st and 2nd     =>  True    (red -> green -> black in the same order)
1st and 3rd     =>  False
2nd and 3rd     =>  False

"""

from itertools import combinations


def main():
    data = [
        ['red', 'green', 'black', 'orange'],
        ['red', 'pink', 'green', 'white', 'black'],
        ['white', 'orange', 'pink', 'black']
    ]

    for l1, l2 in combinations(data, 2):
        common = set(l1) & set(l2)
        print([_ for _ in l1 if _ in common] == [_ for _ in l2 if _ in common])


if __name__ == "__main__":
    main()
