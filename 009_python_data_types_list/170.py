"""

Write a Python program to insert an element in a given list after every nth position.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

'a' after the 2nd element
[1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]

'b' after the 4th element:
[1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]

"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    data = [
        ('a', 2),
        ('b', 4)
    ]

    for c, pos in data:
        lst_cpy = list(lst)
        lst_cpy.insert(pos, c)
        print(lst_cpy)


if __name__ == "__main__":
    main()
