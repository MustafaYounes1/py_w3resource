"""

Remove punctuation from a string.

s = "Hello, world!"     =>  Hello world

"""

from string import punctuation


def main():
    s = "Hello, world!"
    print(s.translate(str.maketrans(dict.fromkeys(punctuation, ""))))


if __name__ == "__main__":
    main()
