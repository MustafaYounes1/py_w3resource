"""

Write a Python program to check whether an alphabet is a vowel or consonant.
Expected Output:

Input a letter of the alphabet: k
k is a consonant.

"""


def main():
    c = input("Enter a character: ")
    print(f"{c} is {['consonant', 'vowel'][c.lower() in 'aeiou']}")


if __name__ == "__main__":
    main()
