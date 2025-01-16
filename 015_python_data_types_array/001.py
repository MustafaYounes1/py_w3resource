"""

Write a Python program to create an array of 5 signed integers [-1, 2, 53, 0, 45].

1. Loop through its items and print them in one line
2. Access the second and forth elements through indexes.

Initialized an array of Int datatype, where each element is of 4 bytes
-1 2 53 0 45
2
0

"""

import array as arr


__type_code_to_ctype = {
    "b": "singed-char",
    "B": "unsigned-Char",
    "u": "wchar_t",
    "w": "PY_UCS4",
    "h": "singed-short",
    "H": "unsigned-Short",
    "i": "singed-int",
    "I": "unsigned-Int",
    "l": "singed-long",
    "L": "unsigned-Long",
    "q": "singed-long-long",
    "Q": "unsigned-Long-long",
    "f": "float",
    "d": "double"
}


def main():
    a = arr.array('i', [-1, 2, 53, 0, 45])
    print(f"Initialized an array of {__type_code_to_ctype[a.typecode]} datatype, "
          f"where each element is of {a.itemsize} bytes")

    for _ in a:
        print(_, end=" ")

    print()
    print(a[1])
    print(a[3])


if __name__ == "__main__":
    main()
