"""

Write a Python program to convert JSON encoded data into Python objects.

json_data = [
    '{"name": "David", "age": 6, "class": "I"}',
    '["Red", "Green", "Black"]',
    '"Python Json"',
    '1234',
    '21.34'
]

{'name': 'David', 'age': 6, 'class': 'I'}
['Red', 'Green', 'Black']
Python Json
1234
21.34

"""

import json


def main():
    json_data = [
        '{"name": "David", "age": 6, "class": "I"}',
        '["Red", "Green", "Black"]',
        '"Python Json"',
        '1234',
        '21.34'
    ]

    for _ in json_data:
        print(json.loads(_))

if __name__ == "__main__":
    main()
