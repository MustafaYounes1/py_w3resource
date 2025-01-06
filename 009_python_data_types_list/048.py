"""

Write a Python program to print nested lists (each list on a new line) using the print() function.
(without using a for loop)

colors = [['Red'], ['Green'], ['Black']]

['Red']
['Green']
['Black']

"""


def main():
    colors = [['Red'], ['Green'], ['Black']]
    print("\n".join(list(map(str, colors))))


if __name__ == "__main__":
    main()
