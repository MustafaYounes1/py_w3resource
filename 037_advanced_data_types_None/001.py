"""

Write a Python function that takes a string as input and returns "None" if the string is empty, otherwise it returns
the given string.

""          =>  None
"test"      =>  test

"""


def validate_string(s: str) -> str | None:
    if not s:
        return None
    else:
        return s


def main():
    data = ["", "test"]

    for _ in data:
        print(validate_string(_))


if __name__ == "__main__":
    main()
