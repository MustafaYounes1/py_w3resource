"""

Write a Python program to replace each character of a word of length five and more with a hash character (#).

Count the lowercase letters in the said list of words:
##### the ######### ####### in the said list of ######

Python - Remove punctuations from a string:
###### - ###### ############ from a #######
"""


def main():
    s = input("Enter a string: ")
    print(" ".join([_ if len(_) < 5 else '#' * len(_) for _ in s.split()]))


if __name__ == "__main__":
    main()
