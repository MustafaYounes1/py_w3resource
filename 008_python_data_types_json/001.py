"""

Write a Python program to convert JSON data to Python object.

json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'

Name:  David
Class:  I
Age:  6

"""

import json


def main():
    json_obj = '{ "Name":"David", "Class":"I", "Age":6 }'
    py_obj = json.loads(json_obj)
    for k, v in py_obj.items():
        print(k, ': ', v)


if __name__ == "__main__":
    main()
