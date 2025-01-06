"""

Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
If the string length is less than 2, return the empty string instead.

Sample String : 'w3resource'
Expected Result : 'w3ce'

Sample String : 'w3'
Expected Result : 'w3w3'

Sample String : ' w'
Expected Result : Empty String

"""


def main():
    s = input("Enter a string: ").strip()

    if len(s) < 2:
        print("Empty string")
    else:
        print(s[:2] + s[-2:])


if __name__ == "__main__":
    main()
