"""

Write a Python program to move spaces to the front of a given string.

"w3resource .  com  "   =>  "     w3resource.com"

"""


def main():
    s = "w3resource .  com  "
    print(" " * s.count(" ") + s.replace(" ", ""))


if __name__ == "__main__":
    main()
