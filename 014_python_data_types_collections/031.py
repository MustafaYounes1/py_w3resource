"""

Write a Python program to count the most common 4 words in a list.

words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]

[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]

"""

from collections import Counter


def main():
    words = [
        'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
        'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
        'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
        'white', 'orange', "orange", 'red'
    ]

    c = Counter(words)
    print(c.most_common(4))


if __name__ == "__main__":
    main()
