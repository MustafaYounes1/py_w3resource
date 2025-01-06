"""

Write a Python program to convert Python objects into JSON strings. Print all the values.

py_objs = [
    {"name": "David", "age": 6, "class": "I"},
    ["Red", "Green", "Black"],
    "Python Json",
    1234,
    21.34,
    True,
    False,
    None
    ]

{"name": "David", "age": 6, "class": "I"}
["Red", "Green", "Black"]
"Python Json"
1234
21.34
true
false
null

"""

import json


def main():
    py_objs = [
        {"name": "David", "age": 6, "class": "I"},
        ["Red", "Green", "Black"],
        "Python Json",
        1234,
        21.34,
        True,
        False,
        None
    ]

    for _ in py_objs:
        print(json.dumps(_))


if __name__ == "__main__":
    main()
