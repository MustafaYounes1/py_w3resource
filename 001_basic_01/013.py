"""

Write a Python program to print the following 'here document'.

Sample string:
==============
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

"""


def main():
    # define a multi-line string, also known as a heredoc string
    string = """a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
    """
    print(string)


if __name__ == "__main__":
    main()
