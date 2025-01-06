"""

Write a Python program to remove all strings from a given list of tuples.

[(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
[(100,), (80,), (90,), (88, 89), (90, 92)]

"""


def main():
    lst = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
    print(
        [tuple(__ for __ in _ if not isinstance(__, str)) for _ in lst]
    )


if __name__ == "__main__":
    main()
