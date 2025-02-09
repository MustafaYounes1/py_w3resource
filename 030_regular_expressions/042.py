"""

Write a Python program to find URLs in a string.

'<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'

['https://w3resource.com', 'http://github.com']

"""

import re


def main():
    s = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
    print(re.findall(r'href="(.+?)"', s))


if __name__ == "__main__":
    main()
