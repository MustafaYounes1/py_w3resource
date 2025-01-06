"""

Write a Python program to remove all vowels from a given string.

Original string: Python     =>  Pythn
Original string: C Sharp    =>  C Shrp
Original string: JavaScript =>  JvScrpt

"""

import re


__vowels = {'a', 'e', 'i', 'o', 'u'}


def main():
    s = input("Enter a string: ")

    print(
        "".join(
            list(map(lambda x: x if x not in __vowels else "", s))
        )
    )

    # or
    # print(
    #     re.sub(r'[aeiou]+', '', s, flags=re.IGNORECASE)
    # )


if __name__ == "__main__":
    main()
