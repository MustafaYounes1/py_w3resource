"""

Write a Python program to find the name of the oldest student in a given dictionary containing the names and ages of
a group of students.

{
    "Bernita Ahner": 12,
    "Kristie Marsico": 11,
    "Sara Pardee": 14,
    "Fallon Fabiano": 11,
    "Nidia Dominique": 15
}   =>  Nidia Dominique

{
    "Nilda Woodside": 12,
    "Jackelyn Pineda": 12.2,
    "Sofia Park": 12.4,
    "Joannie Archibald": 12.6,
    "Becki Saunder": 12.7
}   =>  Becki Saunder

"""

__dict_1 = {
    "Bernita Ahner": 12,
    "Kristie Marsico": 11,
    "Sara Pardee": 14,
    "Fallon Fabiano": 11,
    "Nidia Dominique": 15
}

__dict_2 = {
    "Nilda Woodside": 12,
    "Jackelyn Pineda": 12.2,
    "Sofia Park": 12.4,
    "Joannie Archibald": 12.6,
    "Becki Saunder": 12.7
}


def oldest(d: dict):
    return max(d, key=d.get)


def main():
    for d in (__dict_1, __dict_2):
        print(oldest(d))


if __name__ == "__main__":
    main()
