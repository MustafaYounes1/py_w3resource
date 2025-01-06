"""

Write a Python program to insert a specified element in a given list after every nth element.

[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]

Insert 20 in said list after every 4th element:
[1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']

Insert Z in said list after every 3th element:
['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']

"""


def main():
    data = [
        ([1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0], 20, 4),
        (['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd'], 'Z', 3),
    ]

    for lst, el, pos in data:
        res = []

        for idx in range(0, len(lst), pos):
            t = lst[idx: idx + pos]
            res += t
            if len(t) == pos:
                res += [el]

        print(res)


if __name__ == "__main__":
    main()
