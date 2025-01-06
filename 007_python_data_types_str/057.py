"""

Write a Python program to remove spaces from a given string.

w 3 res ou r ce     =>  w3resource

"""


def main():
    s = "w 3 res ou r ce"
    print(s.replace(" ", ""))


if __name__ == "__main__":
    main()
