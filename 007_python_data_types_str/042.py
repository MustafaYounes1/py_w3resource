"""

Write a Python program to count repeated characters in a string.

Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2

"""

from collections import Counter


def main():
    s = "thequickbrownfoxjumpsoverthelazydog"
    for k, v in Counter(s).items():
        if v != 1:
            print(k, v)


if __name__ == "__main__":
    main()
