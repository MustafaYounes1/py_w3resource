"""

Write a Python program to generate Bigrams of words from a given list of strings.

From Wikipedia:
A bigram or digram is a sequence of two adjacent elements from a string of tokens, which are typically letters,
syllables, or words. A bigram is an n-gram for n=2. The frequency distribution of every bigram in a string is commonly
used for simple statistical analysis of text in many applications, including in computational linguistics,
cryptography, speech recognition, and so on.

['Sum all the items in a list', 'Find the second smallest number in a list']

[
    ('Sum', 'all'), ('all', 'the'), ('the', 'items'), ('items', 'in'), ('in', 'a'), ('a', 'list'), ('Find', 'the'),
    ('the', 'second'), ('second', 'smallest'), ('smallest', 'number'), ('number', 'in'), ('in', 'a'), ('a', 'list')
]

"""


def main():
    lst = ['Sum all the items in a list', 'Find the second smallest number in a list']
    print(
        [(a, b) for _ in lst for a, b in zip(_.split()[0:-1], _.split()[1::])]
    )


if __name__ == "__main__":
    main()
