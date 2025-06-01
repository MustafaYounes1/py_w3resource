"""

Write a Python function that calculates the symmetric difference between two frozenset instances.

[1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8] =>  {1, 2, 3, 7, 8}

"""


def main():
    s1, s2 = frozenset([1, 2, 3, 4, 5, 6]), frozenset([4, 5, 6, 7, 8])
    print(s1 ^ s2)


if __name__ == "__main__":
    main()
