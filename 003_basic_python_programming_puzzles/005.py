"""

Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.

['a', 'abb', 'sfs', 'oo', 'de', 'sfde']                                     =>  True
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']                                     =>  False
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']       =>  False
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']  =>  True

"""


__data = [
    ['a', 'abb', 'sfs', 'oo', 'de', 'sfde'],
    ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde'],
    ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew'],
    ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
]


def main():
    for _ in __data:
        print(_[-2] in _[-1] and _[-2] != _[-1])


if __name__ == "__main__":
    main()
