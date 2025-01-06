"""

Write a Python program to generate two strings from a given string. For the first string, use the characters that
occur only once, and for the second, use the characters that occur multiple times in the said string.

aabbcceffgh     =>  egh,    abcf
w3resource      =>  3cosuw, er

"""

from collections import Counter


def main():
    s = input("Enter a string: ")
    s1, s2 = "", ""

    for k, v in Counter(s).items():
        if v == 1:
            s1 += k
        else:
            s2 += k

    print(s1, s2)

if __name__ == "__main__":
    main()
