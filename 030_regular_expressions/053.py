"""

Write a Python program to concatenate the consecutive numbers in a given string.

Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready.

Enter at 120 Kearny Street. The security desk can direct you to floor 16. Please have your identification ready.

"""

import re


def main():
    s = ("Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. "
         "Please have your identification ready.")

    print(re.sub(r"(\d+)\s(\d+)", r"\1\2", s))


if __name__ == "__main__":
    main()
