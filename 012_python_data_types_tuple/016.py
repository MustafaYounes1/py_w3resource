"""

Write a Python program to convert a tuple to a dictionary.
Note: use the second element from each pair as the key and the first one as the value

((2, "w"), (3, "r"))

{'w': 2, 'r': 3}

"""


def main():
    t = ((2, "w"), (3, "r"))
    print({e2: e1 for e1, e2 in t})


if __name__ == "__main__":
    main()
