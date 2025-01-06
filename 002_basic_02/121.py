"""

Write a Python program to create a coded string from a given string, using a specified formula.
Replace all 'P' with '9', 'T' with '0', 'S' with '1', 'H' with '6' and 'A' with '8'

Original string: PHP            =>  969
Original string: JAVASCRIPT     =>  J8V81CRI90

"""

__coding = {
    "P": "9",
    "T": "0",
    "S": "1",
    "H": "6",
    "A": "8"
}


def main():
    s = input("Enter a string: ")

    out_str = "".join(map(lambda x: __coding.get(x, x), s))

    # or
    out_str = s.translate(str.maketrans("PTSHA", "90168"))

    print(out_str)


if __name__ == "__main__":
    main()
