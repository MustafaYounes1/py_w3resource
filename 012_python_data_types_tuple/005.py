"""

Write a Python program to add an item to a tuple.

t = (4, 6, 2, 8, 3, 1)

First add 9 the end of it
Then these items (15, 20, 25) after the third element
And finally add 0 at the beginning

(0, 4, 6, 2, 15, 20, 25, 8, 3, 1, 9)

"""


def main():
    t = (4, 6, 2, 8, 3, 1)

    t += (9, )
    t = t[:3] + (15, 20, 25) + t[3:]
    t = (0, ) + t

    print(t)


if __name__ == "__main__":
    main()
