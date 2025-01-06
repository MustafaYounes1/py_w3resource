"""

Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.

    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }

    "2 3" => dg dh di eg eh ei fg fh fi

"""

from itertools import product


def main():
    string_maps = {
        1: "abc",
        2: "def",
        3: "ghi",
        4: "jkl",
        5: "mno",
        6: "pqrs",
        7: "tuv",
        8: "wxy",
        9: "z"
    }

    a, b = [int(_) for _ in input("Enter two space-separated integers between 1 and 9: ").split()]
    assert 0 < a < 10 and 0 < b < 10, "invalid inputs"

    for _ in product(string_maps[a], string_maps[b]):
        print("".join(_))


if __name__ == "__main__":
    main()
