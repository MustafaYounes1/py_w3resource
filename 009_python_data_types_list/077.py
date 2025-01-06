"""

Write a Python program to decode a run-length message.

[[2, 1], 2, 3, [2, 4], 5, 1]

[1, 1, 2, 3, 4, 4, 5, 1]

"""


def decode(el):
    if isinstance(el, list):
        return [el[1]] * el[0]
    else:
        return [el]


def main():
    lst = [[2, 1], 2, 3, [2, 4], 5, 1]
    print(
        [__ for _ in lst for __ in decode(_)]
    )


if __name__ == "__main__":
    main()
