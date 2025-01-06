"""

Write a Python program to find a string which, when each character is shifted (ASCII decremented) by shift,
gives the result.

Input:
Ascii character table
Shift = 1
Output:
@rbhhbg`q`bsdqs`akd

Input:
Ascii character table
Shift = -1
Output:
Btdjj!dibsbdufs!ubcmf

"""


__data = [
    ("Ascii character table", 1),
    ("Ascii character table", -1)
]


def main():
    for s, shift in __data:
        print(
            "".join(chr(ord(c) - shift) for c in s)
        )


if __name__ == "__main__":
    main()
