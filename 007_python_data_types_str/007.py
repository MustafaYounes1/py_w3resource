"""

Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'

Expected Result : 'The lyrics is good!'
'The lyrics is poor!'

"""


def main():
    s = '''The lyrics is not that poor!
The lyrics is poor!'''

    i0 = s.find('not')
    i1 = s.find('poor')

    if i1 > i0:
        print(s.replace(s[i0: i1 + 4], 'good'))

    else:
        print(s)


if __name__ == "__main__":
    main()
