"""

Write a Python program to reverse all words of even lengths.

Sample Input:
("The quick brown fox jumps over the lazy dog")     =>  The quick brown fox jumps revo the yzal dog
("Python Exercises")                                =>  nohtyP Exercises

"""


def main():
    s = input("Enter a string of words: ")
    new_words = [i[::-1] if not len(i) % 2 else i for i in s.split()]
    print(' '.join(new_words))


if __name__ == "__main__":
    main()
