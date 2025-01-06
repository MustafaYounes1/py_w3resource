"""

Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas
if there is a comma, otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).

Input:
a b c d
Output:
['a', 'b', 'c', 'd']

Input:
a,b,c,d
Output:
['a', 'b', 'c', 'd']

Input:
abcd
Output:
['b', 'd']

"""


def main():
    s = input("Enter a string: ")

    if " " in s:
        print(s.split())

    elif "," in s:
        print(s.split(","))

    else:
        print(list(s[1::2]))


if __name__ == "__main__":
    main()
