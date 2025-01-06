"""

Write a Python program to convert a Unicode list to a list of strings.

[u'S001', u'S002', u'S003', u'S004']
['S001', 'S002', 'S003', 'S004']

"""


def main():
    lst = [u'S001', u'S002', u'S003', u'S004']
    print(list(map(str, lst)))


if __name__ == "__main__":
    main()
