"""

Write a Python program that takes a string and returns # on both sides of each element, which are not vowels.

Green       -> "-G--r-ee-n-"
White       -> "-W--h-i-t-e"
aeiou       -> "aeiou"

"""


def main():
    s = input("Enter a string: ")
    print("".join([f"-{_}-" if _.lower() not in "aeiou" else _ for _ in s]))


if __name__ == "__main__":
    main()
