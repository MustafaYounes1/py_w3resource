"""

Write a Python program to clone of a tuple.

t = ("HELLO", 5, [], True)

"""

from copy import deepcopy


def main():
    t = ("HELLO", 5, [], True)
    t0 = deepcopy(t)
    t0[2].append(1)
    print(t, t0)


if __name__ == "__main__":
    main()
