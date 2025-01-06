"""

Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is".

"""


def main():
    string = input("Enter a string: ")
    if string.startswith("Is"):
        print(string)
    else:
        print(f"Is{string}")


if __name__ == "__main__":
    main()
