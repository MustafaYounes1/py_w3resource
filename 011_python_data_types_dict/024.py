"""

Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.

'w3resource'

{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

"""

from collections import Counter


def main():
    s = 'w3resource'
    print(dict(Counter(s)))


if __name__ == "__main__":
    main()
