"""

Write a Python program to count the most and least common characters in a given string.

hello world

Most  common:  l
Least common:  h

"""

from collections import Counter


def main():
    s = 'hello world'
    s = s.replace(" ", "")
    c = Counter(s)

    print(f"Most  common:  {max(c, key=c.get)}")
    print(f"Least common:  {min(c, key=c.get)}")


if __name__ == "__main__":
    main()
