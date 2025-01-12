"""

Write a Python program to remove an item from a set if it is present in the set.

0, 1, 2, 3, 4, 5

Remove the following items from the set continuously:

0   =>  {1, 2, 3, 4, 5}
5   =>  {1, 2, 3, 4}
7   =>  {1, 2, 3, 4}

"""


def main():
    s = {0, 1, 2, 3, 4, 5}
    items = (0, 5, 7)
    for _ in items:
        s.discard(_)
        print(s)


if __name__ == "__main__":
    main()
