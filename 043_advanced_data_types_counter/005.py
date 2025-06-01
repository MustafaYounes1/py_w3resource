"""

Write a Python program that creates a counter of the words in a sentence and prints the words in ascending and
descending order of their frequency.

"Red Green Black Black Red red Orange Pink Pink Red White."

ascending:  ['white', 'orange', 'green', 'pink', 'black', 'red']
descending: ['red', 'black', 'pink', 'green', 'orange', 'white']

"""

from collections import Counter
from operator import itemgetter
from string import digits, punctuation


def main():
    sentence = "Red Green Black Black Red red Orange Pink Pink Red White."
    c = Counter(sentence.translate(str.maketrans("", "", digits + punctuation)).lower().split())

    most_cmn_words = c.most_common()
    print(list(map(itemgetter(0), most_cmn_words[::-1])))  # ascending order
    print(list(map(itemgetter(0), most_cmn_words)))  # descending order


if __name__ == "__main__":
    main()
