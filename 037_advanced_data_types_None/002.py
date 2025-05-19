"""

Write a Python function that returns the middle character of a string or "None" if the string length is odd.

abcd    =>  None
abcde   =>  c

"""


def middle_char(s: str) -> str | None:
    if len(s) % 2 == 0:
        return None
    else:
        return s[len(s) // 2]


def main():
    data = ["abcd", "abcde"]

    for _ in data:
        print(middle_char(_))


if __name__ == "__main__":
    main()
