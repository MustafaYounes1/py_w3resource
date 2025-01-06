"""

Write a Python program to split a string on the last occurrence of the delimiter.

"w,3,r,e,s,o,u,r,c,e"

['w,3,r,e,s,o,u,r,c', 'e']

"""


def main():
    s = "w,3,r,e,s,o,u,r,c,e"
    print(s.rsplit(",", maxsplit=1))


if __name__ == "__main__":
    main()
