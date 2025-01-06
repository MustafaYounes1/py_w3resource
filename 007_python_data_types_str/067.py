"""

Write a Python program to remove all consecutive duplicates of a given string.

aaaaebbbb       =>  aeb
xxxxxyyyyy      =>  xy
xxxxxyyyyyxx    =>  xyx

"""

from itertools import groupby


def main():
    s = input("Enter a string: ")
    out = "".join([s[0]] + [_ for idx, _ in enumerate(s[1:], start=1) if _ != s[idx - 1]])
    print(out)

    # or using itertools groupby
    out = []
    for k, g in groupby(s):
        out.append(k)

    print("".join(out))


if __name__ == "__main__":
    main()
