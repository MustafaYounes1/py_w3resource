"""

Write a Python program to count the number of unique sublists within a given list.

[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
{('green', 'orange'): 2, ('black',): 1, ('white',): 1}

"""

from collections import Counter


def main():
    data = [
        [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],
        [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    ]

    for _ in data:
        print(dict(Counter(list(map(tuple, _)))))


if __name__ == "__main__":
    main()
