"""

Write a Python program to find items starting with a specific character from a list.

['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

a   =>  ['abcd', 'abc', 'acjd']
d   =>  ['dagfa']
w   =>   []

"""


def main():
    lst = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
    for c in ('a', 'd', 'w'):
        print([_ for _ in lst if _.startswith(c)])


if __name__ == "__main__":
    main()
