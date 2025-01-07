"""

Write a Python function to check if a list is a palindrome or not.

[1, 2, 4, 3, 5, 4, 6, 9, 2, 1]  =>  False
[1, 2, 2, 1]                    =>  True
['Red', 'Green', 'Blue']        =>  False
['Red', 'Green', 'Red']         =>  True

"""


def main():
    data = [
        [1, 2, 4, 3, 5, 4, 6, 9, 2, 1],
        [1, 2, 2, 1],
        ['Red', 'Green', 'Blue'],
        ['Red', 'Green', 'Red']
    ]

    for lst in data:
        print(lst == lst[::-1])


if __name__ == "__main__":
    main()
