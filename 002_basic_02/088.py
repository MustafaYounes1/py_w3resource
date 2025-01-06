"""

Write a Python program that accepts two strings and determines whether the letters in the second string are present in
the first string.

Sample Input:
["python", "ypth"]      =>  True
["python", "ypths"]     =>  False
["python", "ypthon"]    =>  True
["123456", "01234"]     =>  False
["123456", "1234"]      =>  True

"""


def s2_in_s1(s1, s2):
    return all([_ in s1 for _ in s2])


def main():
    s1, s2 = input("Enter the two space-separated strings: ").split()
    print(s2_in_s1(s1.lower(), s2.lower()))


if __name__ == "__main__":
    main()
