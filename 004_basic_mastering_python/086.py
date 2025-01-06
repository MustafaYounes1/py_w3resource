"""

Check if a string is a valid number.

"""


def main():
    s = "123.45"
    try:
        float(s)
        print(True)
    except ValueError:
        print(False)


if __name__ == "__main__":
    main()
