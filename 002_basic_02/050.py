"""

Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string.

Input:
English letters (including single byte alphanumeric characters, blanks, symbols) are given on one line.
The length of the input character string is 1000 or less.

Input a text with two words 'Python' and 'Java'
Python is popular than Java     =>      Java is popular than Python

"""


def main():
    text = input("Input a text with two words 'Python' and 'Java': ")

    text = text.replace("Python", "*****")
    text = text.replace("Java", "Python")
    text = text.replace("*****", "Java")
    print(text)


if __name__ == "__main__":
    main()
