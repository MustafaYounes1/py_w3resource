"""

Write a Python function that replaces all occurrences of a substring in a string with another substring. Returns None
if the original string is empty.

"Java Exercises!"     (replace Java with Python)      =>   Python Exercises!
""                                                    =>  None

"""

def replace(s: str, org: str, rep: str) -> str | None:
    if not s:
        return None

    return s.replace(org, rep)


def main():
    data = ["Java Exercises!", ""]

    for _ in data:
        print(replace(_, "Java", "Python"))


if __name__ == "__main__":
    main()
