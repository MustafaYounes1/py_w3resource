"""

Write a Python program to remove an empty tuple(s) from a list of tuples.

[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']


"""


def main():
    lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
    print(list(filter(lambda _: _, lst)))


if __name__ == "__main__":
    main()
