"""

Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.

Red Green Black White Pink
Black Green Pink Red White

Calculate the sum of two said numbers given as strings.
Calculate as given numbers of sum said strings. the two

The quick brown fox jumps over the lazy dog.
The brown dog. fox jumps lazy over quick the

"""


def main():
    s = input("Enter a string: ")
    print(" ".join(sorted(s.split(), key=lambda w: w[0])))


if __name__ == "__main__":
    main()
