"""

Write a Python program to find elements in a given set that are not in another set.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

in s1 but not in s2     =>  {1, 2, 3}
in s2 but not in s1     =>  {8, 6, 7}

"""


def main():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}

    # or u can just use s1.difference(s2)
    print(s1 - s2)
    print(s2 - s1)


if __name__ == "__main__":
    main()
