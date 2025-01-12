"""

Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings.
Note: try to use Python sets

['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']

{'Red': 4, 'Green': 2, 'Blue': 1}

"""


def main():
    lst = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
    print({k: lst.count(k) for k in set(lst)})


if __name__ == "__main__":
    main()
