"""

Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary
or list.

users = {
    'Carla ': {
        'name': {
            'first': 'Carla ',
            'last': 'Russell'
        },
        'postIds': [1, 2, 3, 4, 5]
    }
}

['Carla ', 'name', 'last']  =>  Russell
['Carla ', 'postIds', 1]    =>  2

"""

from functools import reduce
from operator import getitem


def main():
    users = {
        'Carla ': {
            'name': {
                'first': 'Carla ',
                'last': 'Russell'
            },
            'postIds': [1, 2, 3, 4, 5]
        }
    }

    selectors = [
        ['Carla ', 'name', 'last'],
        ['Carla ', 'postIds', 1]
    ]

    for selector in selectors:
        print(reduce(lambda a, b: getitem(a, b), selector, users))


if __name__ == "__main__":
    main()
