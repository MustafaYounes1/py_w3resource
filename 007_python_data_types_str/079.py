"""

Write a Python program to find the smallest and largest words in a given string.

Write a Java program to sort an array of given integers using Quick sort Algorithm.

Smallest word:  a
Largest word:   Algorithm.

"""


def main():
    s = input("Enter the string: ")
    words = s.split()
    print(f"Smallest word: {min(words, key=len)}")
    print(f"Largest  word: {max(words, key=len)}")


if __name__ == "__main__":
    main()
