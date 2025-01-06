"""

Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.

Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]

Input: The dance, held in the school gym, ended at midnight.
Output:
[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'],
[' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]

Input: The colors in my studyroom are blue, green, and yellow.
Output:
[['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'],
[' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]

"""

import re


def main():
    s = input("Enter a string: ")
    # By putting [ ,]+ inside parentheses, we are telling re.split to include each separator (comma, space, or their
    # combinations) in the output list. Without parentheses, the separators would be removed entirely during the split.
    print(re.split(r"([ ,]+)", s))


if __name__ == "__main__":
    main()
