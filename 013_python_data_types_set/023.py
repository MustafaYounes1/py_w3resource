"""

Write a Python program to find the longest common prefix of all strings. Use the Python set.

['pqrefgh', 'pqrsfgh']      =>  pqr
['w3r', 'w3resource']       =>  w3r
['Python', 'PHP', 'Perl']   =>  P
['Python', 'HTML', 'PHP']   =>  ''

"""


def main():
    data = [
        ['pqrefgh', 'pqrsfgh'],
        ['w3r', 'w3resource'],
        ['Python', 'PHP', 'Perl'],
        ['Python', 'HTML', 'PHP']
    ]

    for words in data:
        out = ""

        for chars in zip(*words):
            if len(set(chars)) == 1:
                out += chars[0]
            else:
                break

        print(out)


if __name__ == "__main__":
    main()
