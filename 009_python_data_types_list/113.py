"""

Write a Python program to remove duplicate dictionary entries from a given list.

[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

[{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
"""


def main():
    lst = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
    print([dict(_) for _ in {tuple(d.items()) for d in lst}])


if __name__ == "__main__":
    main()
