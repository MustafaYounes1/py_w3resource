"""

Reverse each word in a sentence.

Hello world     =>  olleH dlrow

"""


def main():
    sentence = "Hello world"
    print(" ".join(list(map(lambda x: x[::-1], sentence.split()))))


if __name__ == "__main__":
    main()
