"""

Write a Python program to deserialize the following json data.

'{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'

{'a': 4, 'b': 2}

"""

import json


def main():
    json_data = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
    print(json.loads(json_data))


if __name__ == "__main__":
    main()
