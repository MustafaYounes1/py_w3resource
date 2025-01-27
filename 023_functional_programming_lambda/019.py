"""

Write a Python program to find all anagrams of a string in a given list of strings using Lambda.

'abcd', ['bcda', 'abce', 'cbda', 'cbea', 'adcb']    =>  ['bcda', 'cbda', 'adcb']

"""

from collections import Counter


def main():
    s, lst = 'abcd', ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
    print(list(filter(lambda _: Counter(_) == Counter(s), lst)))


if __name__ == "__main__":
    main()
