"""

Write a Python program that takes a user's input and converts it to uppercase. If the input is empty, return None.

"""

def validated_prompt() -> str | None:
    p = input("Inter something: ")
    if not p:
        return None
    else:
        return p.upper()


def main():
    print(validated_prompt())


if __name__ == "__main__":
    main()
