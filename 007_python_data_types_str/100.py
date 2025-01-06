"""

Write a Python program to check whether all words in a given string does not contain duplicate characters.
Return True or False.

Filter out the factorials of the said list.     =>  False
Python Exercise.                                =>  False
The wait is over.                               =>  True

"""


def main():
    s = input("Enter a sentence: ")
    print(all(len(_) == len(set(_)) for _ in s.split()))


if __name__ == "__main__":
    main()
