"""

Write a Python program to remove repeated consecutive characters and replace them with single letters and print a
updated string.


Red Green White     -> "Red Gren White"
aabbbcdeffff        -> "abcdef"
Yellowwooddoor      -> "Yelowodor"

"""


def main():
    s = input("Enter a string: ")
    print(s[0] + "".join([s[i]for i in range(1, len(s)) if s[i] != s[i - 1]]))


if __name__ == "__main__":
    main()
