"""

Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5

"""


def main():
    for _ in range(6):
        if _ == 3:
            continue
        else:
            print(_, end=" ")


if __name__ == "__main__":
    main()
