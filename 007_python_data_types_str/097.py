"""

Write a Python program to convert a given Camel string to Snake case.

Snake case (stylized as snake_case) refers to the style of writing in which each space is replaced by an underscore
(_) character, and the first letter of each word written in lowercase. It is a commonly used naming convention in
computing, for example for variable and subroutine names, and for filenames. One study has found that readers can
recognize snake case values more quickly than camel case.

'JavaScript'        java_script
'FooBar'            foo_bar

"""

import re


def main():
    s = ["JavaScript", "FooBar"]
    for _ in s:
        print(
            "_".join(re.findall(r"[A-Z][a-z]+", _)).lower()
        )


if __name__ == "__main__":
    main()
