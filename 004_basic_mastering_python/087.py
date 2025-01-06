"""

Find the length of the longest word in a sentence.

sentence = "The quick brown fox jumps over the lazy dog"    =>  5

"""


def main():
    sentence = "The quick brown fox jumps over the lazy dog"
    print(len(max(sentence.split(), key=len)))


if __name__ == "__main__":
    main()
