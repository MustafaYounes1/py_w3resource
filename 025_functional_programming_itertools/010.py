"""

Write a Python program to generate combinations of a given length of a given iterable.

"Python", 1                 =>  [('P',), ('y',), ('t',), ('h',), ('o',), ('n',)]
['A', 'B', 'C', 'D'], 2     =>  [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

"""

from itertools import combinations


def main():
    print(list(combinations("Python", 1)))
    print(list(combinations(['A', 'B', 'C', 'D'], 2)))


if __name__ == "__main__":
    main()
