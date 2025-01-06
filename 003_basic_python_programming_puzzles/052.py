"""

Write a Python program to reverse the case of all strings. For those strings, which contain no letters,
reverse the strings.

Original list:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '', 'FOO', 'UNIQUE']

Original list:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
['gREEN', 'rED', 'oRANGE', 'yELLOW', '', 'wHITE']

Original list:
['Hello', '!@#', '!@#$', '123#@!']
['hELLO', '#@!', '$#@!', '!@#321']

"""


__data = [
    ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique'],
    ['Green', 'Red', 'Orange', 'Yellow', '', 'White'],
    ['Hello', '!@#', '!@#$', '123#@!']
]


def main():
    for sample in __data:
        print(
            [_.swapcase() if _.isalpha() else _[::-1] for _ in sample]
        )


if __name__ == "__main__":
    main()
