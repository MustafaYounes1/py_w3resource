"""

Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

'aza'           =>  True
'madam'         =>  True
'nurses run'    =>  True
"""


def is_palindrome(s: str) -> bool:
    return s.replace(" ", "") == s[::-1].replace(" ", "")


def main():
    print(is_palindrome("aza"))
    print(is_palindrome("madam"))
    print(is_palindrome("nurses run"))


if __name__ == "__main__":
    main()
