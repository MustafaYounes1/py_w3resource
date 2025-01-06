"""

Write a Python program to count the number of each alphabet character in a text file '007.txt'.

"""

from collections import Counter
import pathlib
import string

__input_file = '007.txt'


def main():
    assert pathlib.Path(__input_file).is_file(), f"{__input_file} does not exist."
    with open(__input_file, 'r') as f:
        contents = f.read()

    for _ in string.punctuation + " \n":
        contents = contents.replace(_, "")

    c = Counter(contents.lower())
    for k,v in c.items():
        print(k, v)



if __name__ == "__main__":
    main()
