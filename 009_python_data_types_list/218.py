"""

Write a Python program to sort one list based on another list containing the desired indexes.

l1 = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
l2 = [3, 2, 6, 4, 1, 5]

Note: The second list tells the desired order

ascending order:    ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
descending order:   ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']

"""

from operator import  itemgetter


def main():
    l1 = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
    l2 = [3, 2, 6, 4, 1, 5]

    for r in (False, True):
        print(
            [val for (idx, val) in sorted(zip(l2, l1) , key=itemgetter(0), reverse=r)]
        )


if __name__ == "__main__":
    main()
