"""

Write a Python program to get the memory address of an integer and a string and print its hexadecimal representation

"""


def main():
    n = 10
    print(f"{id(n):X}")

    s = "w3resource"
    print(f"{id(s):X}")


if __name__ == "__main__":
    main()
