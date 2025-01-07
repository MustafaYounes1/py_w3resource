"""

Write a Python program to print a dictionary line by line.

students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

Aex
class     : V
roll_id   : 2
Puja
class     : V
roll_id   : 3

"""


def main():
    students = {
        'Aex': {'class': 'V', 'roll_id': 2},
        'Puja': {'class': 'V', 'roll_id': 3}
    }

    for k in students:
        print(k)
        for kk, v in students[k].items():
            print(f"{kk:10}: {v}")


if __name__ == "__main__":
    main()
