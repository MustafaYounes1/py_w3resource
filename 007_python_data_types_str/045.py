"""

Write a Python program to check whether a string contains all letters of the alphabet.

The quick brown fox jumps over the lazy dog     =>  True
The quick brown fox jumps over the lazy cat     =>  False

"""

from string import ascii_lowercase


def main():
    s = input("Enter a string: ")
    print(set((_.lower() for _ in s if _.lower() in ascii_lowercase)) == set(ascii_lowercase))


if __name__ == "__main__":
    main()
