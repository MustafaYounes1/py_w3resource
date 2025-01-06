"""

Write a Python program to convert Python object to JSON data.

python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}

{"name": "David", "class": "I", "age": 6}

"""

import json


def main():
    python_obj = {
        "name": "David",
        "class": "I",
        "age": 6
    }
    json_obj = json.dumps(python_obj)
    print(json_obj)


if __name__ == "__main__":
    main()
