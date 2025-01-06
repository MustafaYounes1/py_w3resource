"""

Write a Python program to concatenate element-wise three given lists.

['0', '1', '2', '3', '4']
['red', 'green', 'black', 'blue', 'white']
['100', '200', '300', '400', '500']

['0red100', '1green200', '2black300', '3blue400', '4white500']

"""


def main():
    data = [
        ['0', '1', '2', '3', '4'],
        ['red', 'green', 'black', 'blue', 'white'],
        ['100', '200', '300', '400', '500']
    ]

    print([a + b + c for a, b, c in zip(*data)])


if __name__ == "__main__":
    main()
