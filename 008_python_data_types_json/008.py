"""

Write a Python program to check whether a JSON string contains complex object or not.
If the json object contains the '__complex__' key => parse it as a python complex object, otherwise, parse it as
a dict

'{"__complex__": true, "real": 4, "img": 5}'        =>  (4+5j)
'{"real": 4, "img": 3}'                             =>  {'real': 4, 'img': 3}

"""

import json


def parse_complex(j_data: dict):
    if '__complex__' in j_data:
        return complex(j_data["real"], j_data["img"])

    else:
        return j_data


def main():
    json_data = [
        '{"__complex__": true, "real": 4, "img": 5}',
        '{"real": 4, "img": 3}'
    ]

    for _ in json_data:
        print(json.loads(_, object_hook=parse_complex))


if __name__ == "__main__":
    main()
