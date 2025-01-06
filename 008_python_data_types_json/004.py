"""

Write a Python program to convert Python dictionary object (sort by key) to JSON data.
Print the object members with indent level 4

py_dict = {'4': 5, '6': 7, '1': 3, '2': 4}

{
    "1": 3,
    "2": 4,
    "4": 5,
    "6": 7
}

"""

import json


def main():
    py_dict = {'4': 5, '6': 7, '1': 3, '2': 4}
    json_obj = json.dumps(py_dict, indent=4, sort_keys=True)
    print(json_obj)


if __name__ == "__main__":
    main()
