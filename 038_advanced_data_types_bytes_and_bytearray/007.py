"""

Write a Python program that checks if two bytes objects are equal.

b'Python', b'Pytho'     =>  False
b'Python', b'Python'    =>  True

"""


def main():
    print(b'Python' == b'Pytho')
    print(b'Python' == b'Python')


if __name__ == "__main__":
    main()
