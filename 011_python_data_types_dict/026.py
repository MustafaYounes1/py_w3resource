"""

Write a Python program to sum the values associated with a key in a dictionary.

student = [
        {'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}
]

'id'        =>  6
'success'   =>  2

"""

from operator import itemgetter


def main():
    student = [
        {'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}
    ]

    for k in ('id', 'success'):
        print(sum(map(itemgetter(k), student)))


if __name__ == "__main__":
    main()
