"""

Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number

W3resource  =>  True

"""


def main():
    s = input("Enter a string: ")
    print(
        any(_ for _ in s if _.islower()) and
        any(_ for _ in s if _.isupper()) and
        any(_ for _ in s if _.isdigit())
    )


if __name__ == "__main__":
    main()
