"""

Write a Python program to get the maximum and minimum values of a dictionary.

my_dict = {'x': 500, 'y': 5874, 'z': 560}

Min : 500
Max : 5874

"""


def main():
    my_dict = {'x': 500, 'y': 5874, 'z': 560}
    print(f"Min : {min(my_dict.values())}")
    print(f"Max : {max(my_dict.values())}")


if __name__ == "__main__":
    main()
