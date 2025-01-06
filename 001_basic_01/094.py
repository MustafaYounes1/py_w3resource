"""

Write a Python program to convert the bytes in a given string to a list of integers.

x = b'Abc'

"""


def main():
    # str = '...' literals = a sequence of characters. A “character” is a basic unit of text: a letter, digit,
    # punctuation mark, symbol, space, or “control character” (like tab or backspace).
    # The Unicode standard assigns each character to an integer code point between 0 and 0x10FFFF.

    # bytes = b'...' literals = a sequence of bytes. A “byte” is the smallest integer type addressable on a computer,
    # which is nearly universally an octet, or 8-bit unit, thus allowing numbers between 0 and 255.

    # By adding the ‘b’ character before a string literal, it becomes a bytes literal.

    # adding the ‘b’ character before a string literal creates a bytes literal. This means that the string content
    # should be considered as a series of bytes and not characters. Bytes literals are utilized for representing
    # binary data like encoded text, pictures, audio, or any other type of data that may not directly correspond
    # to characters.

    x = b'Abc'
    print(list(x))


if __name__ == "__main__":
    main()
