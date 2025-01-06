"""

Write a Python program to remove the nth index character from a nonempty string.

'Python', 0     =>  ython
'Python', 3     =>  Pyton
'Python', 5     =>  Pytho

"""


def main():
    s = input("Enter a string: ")
    n = int(input("Enter the idx: "))
    print(s.replace(s[n], ""))


if __name__ == "__main__":
    main()
