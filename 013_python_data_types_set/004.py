"""

Write a Python program to remove item(s) from a given set.

0, 1, 3, 4, 5

1. start with removing a random item
2. remove 1, but keep in mind that it could be removed from the set in the previous step

Expect the list to have only 3 items with no KeyErrors being raised

"""


def main():
    s = {0, 1, 3, 4, 5}
    s.remove(1)
    s.remove(1)
    print(s)


if __name__ == "__main__":
    main()
