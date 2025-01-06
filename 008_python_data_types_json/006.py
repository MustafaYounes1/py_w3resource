"""

Write a Python program to create a new JSON file from an existing JSON file.

Load '006.json' and delete the key 'abbreviation' from all states and write the result to '006_out.json'

"""

import json


def main():
    with open('006.json', 'r') as f:
        contents = json.load(f)

    for _ in contents['states']:
        del _["abbreviation"]

    with open('006_out.json', 'w') as f:
        json.dump(contents, f, sort_keys=True, indent=4)


if __name__ == "__main__":
    main()
