"""

Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

"""


def main():
    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    print(dict(zip(keys, values)))


if __name__ == "__main__":
    main()
