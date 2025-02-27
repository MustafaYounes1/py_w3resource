"""

Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

"""

from collections import Counter


def main():
    s = 'google.com'
    print(dict(Counter(s)))


if __name__ == "__main__":
    main()
