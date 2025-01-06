"""

Write a Python program to check if the first character of each element in a list is the same.

[1234, 122, 1984, 19372, 100]   =>  True
[1234, 922, 1984, 19372, 100]   =>  False
['aabc', 'abc', 'ab', 'a']      =>  True
['aabc', 'abc', 'ab', 'ha']     =>  False

"""


def main():
    data = [
        [1234, 122, 1984, 19372, 100],
        [1234, 922, 1984, 19372, 100],
        ['aabc', 'abc', 'ab', 'a'],
        ['aabc', 'abc', 'ab', 'ha']
    ]

    for lst in data:
        print(len(set(list(map(lambda x: str(x)[0], lst)))) == 1)


if __name__ == "__main__":
    main()
