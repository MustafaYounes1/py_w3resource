"""

Write a Python program to find all words starting with 'a' or 'e' in a given string.

"The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the
ArrayList and the ArrayList is trimmed accordingly."

['example', 'eates', 'an', 'ayList', 'apacity', 'elements', 'elements', 'are', 'en', 'added', 'ayList', 'and',
 'ayList', 'ed', 'accordingly']

"""

import re


def main():
    s = ("The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to "
         "the ArrayList and the ArrayList is trimmed accordingly.")

    print(re.findall(r"[ae]\w+", s))

if __name__ == "__main__":
    main()
