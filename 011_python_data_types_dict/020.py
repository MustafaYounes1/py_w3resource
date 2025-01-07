"""

Write a Python program to print all distinct values in a dictionary.

[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

{'S005', 'S002', 'S007', 'S001', 'S009'}

"""


def main():
    data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
            {"VIII": "S007"}]

    print({__ for _ in data for __ in _.values()})


if __name__ == "__main__":
    main()
