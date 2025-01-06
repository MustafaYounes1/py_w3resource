"""

 Write a Python program to format a specified string and limit the length of a string.

    Original string:    1234567890
    Output string:      123456

"""


def main():
    string = "1234567890"
    print(f"{string:.6s}")
    print("%.6s" % string)


if __name__ == "__main__":
    main()
