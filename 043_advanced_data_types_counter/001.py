"""

Write a Python program to create a 'Counter' of the letters in the string "Python Exercise!".

Counter({'e': 2, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, 'E': 1, 'x': 1, 'r': 1, 'c': 1, 'i': 1, 's': 1})


"""

from collections import Counter


def main():
    c = Counter(filter(lambda char: char.isalpha(), "Python Exercise!"))
    print(c)


if __name__ == "__main__":
    main()
