"""

Write a Python program to test whether a passed letter is a vowel or not.

"""


def main():
    vowels = ('a', 'e', 'i', 'o', 'u')
    c = input("Enter a letter: ")
    if c.lower() in vowels:
        print(f"{c} is vowel")
    else:
        print(f"{c} is not vowel")


if __name__ == "__main__":
    main()
