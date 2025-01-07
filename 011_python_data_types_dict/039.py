"""

Write a Python program to store dictionary data in a JSON file.

    data = {
        'students': [
            {'firstName': 'Nikki', 'lastName': 'Roysden'},
            {'firstName': 'Mervin', 'lastName': 'Friedland'},
            {'firstName': 'Aron ', 'lastName': 'Wilkins'}
        ],
        'teachers': [
            {'firstName': 'Amberly', 'lastName': 'Calico'},
            {'firstName': 'Regine', 'lastName': 'Agtarap'}
        ]
    }

"""

import json


def main():
    data = {
        'students': [
            {'firstName': 'Nikki', 'lastName': 'Roysden'},
            {'firstName': 'Mervin', 'lastName': 'Friedland'},
            {'firstName': 'Aron ', 'lastName': 'Wilkins'}
        ],
        'teachers': [
            {'firstName': 'Amberly', 'lastName': 'Calico'},
            {'firstName': 'Regine', 'lastName': 'Agtarap'}
        ]
    }

    with open("039.json", "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
