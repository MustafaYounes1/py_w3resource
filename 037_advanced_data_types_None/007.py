"""

Write a Python function that counts None values in a list recursively. Return 0 if the list is empty.

[None, "Red", None, 8, None, True]  =>  3
[]                                  =>  0
[1, 2]                              =>  0

"""

def count_nones(lst: list[...]) -> int:
    if not lst:
        return 0

    head, *tail = lst

    if head is None:
        return 1 + count_nones(tail)

    else:
        return count_nones(tail)


def main():
    data = [
        [None, "Red", None, 8, None, True],
        [],
        [1, 2]
    ]

    for _ in data:
        print(count_nones(_))


if __name__ == "__main__":
    main()
