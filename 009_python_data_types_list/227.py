"""

Write a Python program to get the symmetric difference between two lists, after applying the provided function to
each list element of both.

[2.1, 1.2], [2.3, 3.4], floor   =>  [1.2, 3.4]

"""

from math import floor


def main():
    lst1, lst2 = [2.1, 1.2], [2.3, 3.4]
    print({_ for _ in lst1 if floor(_) not in set(map(floor, lst2))}.union(
        {_ for _ in lst2 if floor(_) not in set(map(floor, lst1))}
    ))


if __name__ == "__main__":
    main()
