"""

Write a Python program to check whether a string starts with specified characters.

w3resource.com, w3r     =>  True

"""


def main():
    s = input("Enter a string: ")
    p = input("Enter the prefix: ")
    print(s.startswith(p))


if __name__ == "__main__":
    main()
