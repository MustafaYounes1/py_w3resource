"""

Write a Python program to prove that two string variables of the same value point to the same memory location.

"""


def main():
    s1 = "mustafa"
    s2 = "mustafa"
    print(id(s1) == id(s2))
    print(f"s1 memory address: {hex(id(s1))}")
    print(f"s2 memory address: {hex(id(s2))}")


if __name__ == "__main__":
    main()
