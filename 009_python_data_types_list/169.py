"""

Write a Python program to convert a given list of strings and characters to a single list of characters.

['red', 'white', 'a', 'b', 'black', 'f']

['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']

"""


def main():
    lst = ['red', 'white', 'a', 'b', 'black', 'f']
    print([__ for _ in lst for __ in _])


if __name__ == "__main__":
    main()
