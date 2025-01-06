"""

Write a Python program to create a new string by taking a string, and word by word rearranging its
characters in ASCII order.

Input: Ascii character table        =>  Aciis aaccehrrt abelt
Input: maltos won                   =>  almost now

"""

__data = [
    "Ascii character table",
    "maltos won"
]


def main():
    for sample in __data:
        print(
            " ".join(["".join(sorted(w, key=lambda c: ord(c))) for w in sample.split()])
        )


if __name__ == "__main__":
    main()
