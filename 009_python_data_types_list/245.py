"""

Write a Python program that takes any number of iterable objects or objects with a length property and returns
the longest one.

['this', 'is', 'a', 'Green']        =>  Green
[1, 2, 3], [1, 2], [1, 2, 3, 4, 5]  =>  [1, 2, 3, 4, 5]
[1, 2, 3, 4], 'Red'                 =>  [1, 2, 3, 4]

"""


def main():
    data = [
        ['this', 'is', 'a', 'Green'],
        [[1, 2, 3], [1, 2], [1, 2, 3, 4, 5]],
        [[1, 2, 3, 4], 'Red']
    ]

    for lst in data:
        print(max(lst, key=len))


if __name__ == "__main__":
    main()
