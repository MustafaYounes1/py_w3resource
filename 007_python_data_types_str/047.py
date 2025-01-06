"""

Write a Python program to lowercase the first n characters in a string.

W3RESOURCE.COM, 4   =>  w3reSOURCE.COM

"""


def main():
    s = "W3RESOURCE.COM"
    n = 4
    print(s[:n].lower() + s[n:])


if __name__ == "__main__":
    main()
