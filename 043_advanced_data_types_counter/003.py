"""

Write a Python program that creates a counter of the vowels in the word "Python Exercises".

Counter({'e': 3, 'o': 1, 'i': 1})

"""

from collections import Counter


def main():
    c = Counter(filter(lambda char: char in "aeiou", "Python Exercises".lower()))
    print(c)


if __name__ == "__main__":
    main()
