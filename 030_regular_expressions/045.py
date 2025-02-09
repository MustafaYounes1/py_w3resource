"""

Write a Python program to remove ANSI escape sequences from a string.

"\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"

Input:  "  	google.com 216.58.218.206" (colored)
Output: the same input text but without any color

"""

import re


def main():
    s = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
    print(f"Original text:  {s}")

    ns = re.sub(r"\u001b[^m]*m", "", s)
    print(f"Modified text:  {ns}")


if __name__ == "__main__":
    main()
