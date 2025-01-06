"""

Write a Python program to count the number of strings from a given list of strings.
The string length is 2 or more and the first and last characters are the same.

['abc', 'xyz', 'aba', '1221']     =>  2

"""


def main():
    lst = ['abc', 'xyz', 'aba', '1221']
    print(len([_ for _ in lst if len(_) > 2 and _[0] == _[-1]]))


if __name__ == "__main__":
    main()
