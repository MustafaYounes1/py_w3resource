"""

Write a Python program to check if a dictionary is empty or not.

{}      =>  True
{1: 1}  =>  False

"""


def main():
    data = [
        {},
        {1: 1}
    ]

    for d in data:
        print(not bool(d))


if __name__ == "__main__":
    main()
