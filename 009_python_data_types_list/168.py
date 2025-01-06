"""

Write a Python program to display vertically each element of a given list, or list of lists.

['a', 'b', 'c', 'd', 'e', 'f']
a
b
c
d
e
f

[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
1 4 7
2 5 3
5 8 6

"""


def main():
    data = [
        ['a', 'b', 'c', 'd', 'e', 'f'],
        [[1, 2, 5], [4, 5, 8], [7, 3, 6]]
    ]

    for _ in data:
        for __ in _:
            print(" ".join(list(map(str, __))))

        print("*" * 25)


if __name__ == "__main__":
    main()
