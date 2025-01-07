"""

Write a Python program to count the number of items in a dictionary value that is a list.

d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2'], 1: 1}

    =>  5

"""


def main():
    d = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2'], 1: 1}
    print(sum(map(lambda _: len(_) if isinstance(_, list) else 0, d.values())))


if __name__ == "__main__":
    main()
