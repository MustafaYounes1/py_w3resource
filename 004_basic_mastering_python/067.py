"""

Reverse the words in a sentence.

sentence = "Hello world"    =>  world Hello

"""


def main():
    sentence = "Hello world"
    print(" ".join(sentence.split()[::-1]))


if __name__ == "__main__":
    main()
