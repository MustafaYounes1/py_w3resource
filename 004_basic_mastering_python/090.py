"""

Sort a list of tuples by multiple keys.

lst = [(' Aisha', 'A', 25), (' Remy', 'B', 22), ('Meine', 'A', 28)]
Sort them by the second and third keys

[(' Aisha', 'A', 25), ('Meine', 'A', 28), (' Remy', 'B', 22)]

"""


def main():
    lst = [(' Aisha', 'A', 25), (' Remy', 'B', 22), ('Meine', 'A', 28)]
    print(sorted(lst, key=lambda _: (_[1], _[2])))


if __name__ == "__main__":
    main()
