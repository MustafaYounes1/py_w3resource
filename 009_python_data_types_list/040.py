"""

Write a Python program to split a list based on the first character of a word.

word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

    a
        ask
    b
        be
    c
        call
        come
    d
        do
    f
        feel
        find
    g
        get
        give
        go
    h
        have
    k
        know
    l
        leave
        look
    m
        make
    s
        say
        see
        seem
    t
        take
        tell
        think
    u
        use
    w
        want
        work

"""

from itertools import groupby
from operator import itemgetter


def main():
    word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
                 'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

    for k, v in groupby(sorted(word_list, key=itemgetter(0, 1)), key=itemgetter(0)):
        print(k)
        for _ in list(v):
            print(f"\t{_}")


if __name__ == "__main__":
    main()
