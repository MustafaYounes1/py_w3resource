"""

Write a Python function that takes a list and returns a new list with None inserted between each element.

[2, 4, 6, 8, 10]    =>  [2, None, 4, None, 6, None, 8, None, 10]

"""

def insert_nones(lst: list[...]) -> list[...]:
    res = []

    for i, _ in enumerate(lst):
        res.append(_)
        if i != len(lst) - 1:
            res.append(None)

    return res


def main():
    lst = [2, 4, 6, 8, 10]
    print(insert_nones(lst))


if __name__ == "__main__":
    main()
