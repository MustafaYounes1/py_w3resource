"""

Write a Python program that reads text (only alphabetical characters and spaces) and prints two words.
The first word is the one that appears most often in the text. The second one is the word with the most letters.

Note: A word is a sequence of letters which is separated by the spaces.

Input:
A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text.

Input text: Thank you for your comment and your participation.
Output:     your participation.

"""

from collections import Counter
from string import punctuation, digits


def main():
    text = input("Enter the text: ")

    for _ in punctuation:
        text = text.replace(_, "")

    for _ in digits:
        text = text.replace(_, "")

    c = Counter(text.split())
    lengths = list(map(lambda x: (len(x), x), text.split()))
    print(c.most_common()[0], sorted(lengths, key=lambda x: x[0], reverse=True)[0])


if __name__ == "__main__":
    main()
