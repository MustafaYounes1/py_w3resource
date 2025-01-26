"""

Write a Python program to reverse a string.

"1234abcd"  =>  "dcba4321"

"""


def reverse_str(s: str) -> str:
    return s[::-1]


def main():
    print(reverse_str("1234abcd"))


if __name__ == "__main__":
    main()
