"""

Write a Python program to remove the intersection of a second set with a first set.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

on s1:  {1, 2, 3}
on s2:  {6, 7, 8}

"""


def main():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    common = s1 & s2

    for _ in common:
        s1.remove(_)
        s2.remove(_)

    print(s1)
    print(s2)


if __name__ == "__main__":
    main()
