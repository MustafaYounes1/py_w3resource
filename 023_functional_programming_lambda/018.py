"""

Write a Python program to find palindromes in a given list of strings using Lambda.

['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']     =>  ['php', 'aaa']

"""


def main():
    lst = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
    print(list(filter(lambda _: _ == _[::-1], lst)))


if __name__ == "__main__":
    main()
