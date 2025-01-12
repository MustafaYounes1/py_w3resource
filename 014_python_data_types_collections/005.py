"""

Write a Python program that accepts some words and counts the number of distinct words. Print the number of distinct
words and the number of occurrences of each distinct word according to their appearance.

s =  "Red Green Blue Black White Blue Red Orange"

Total number of distinct words: 8
Red     :  2
Blue    :  2
Green   :  1
Black   :  1
White   :  1
Orange  :  1

"""

from collections import Counter


def main():
    s = "Red Green Blue Black White Blue Red Orange"
    c = Counter(s.split())

    print(f"Total number of distinct words: {len(c)}")
    for w, count in c.most_common():
        print(f"{w:8}: {count:2}")


if __name__ == "__main__":
    main()
