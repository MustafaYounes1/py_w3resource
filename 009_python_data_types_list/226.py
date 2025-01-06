"""

Write a Python program to get a list of elements that exist in both lists, after applying the provided function to
each list element of both.

[2.1, 1.2], [2.3, 3.4], floor   =>  [2.1]

"""

from math import floor


def main():
    lst1, lst2 = [2.1, 1.2], [2.3, 3.4]
    print([_ for _ in lst1 if floor(_) in set(map(floor, lst2))])


if __name__ == "__main__":
    main()
