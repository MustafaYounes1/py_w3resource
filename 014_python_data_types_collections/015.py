"""

Write a Python program to find the most common element in a given list.

['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']    =>  Python

"""

from collections import Counter


def main():
    c = Counter(['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python'])
    print(c.most_common(1)[0][0])


if __name__ == "__main__":
    main()
