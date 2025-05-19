"""

Write a Python program that iterates through a list of strings and prints each string. If a string is empty, print
"None" instead.

["Python", "", "Java", "C++", "", "C#"]     =>  ['Python', None, 'Java', 'C++', None, 'C#']

"""


def validate_str(s: str) -> str | None:
    if isinstance(s, str) and s:
        return s
    else:
        return None


def main():
    lst = ["Python", "", "Java", "C++", "", "C#"]
    print(list(map(validate_str, lst)))


if __name__ == "__main__":
    main()
