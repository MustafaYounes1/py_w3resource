"""

Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user
cancels the input.

"""


def main():
    try:
        n = int(input("Enter a number: "))
        print(n)

    except ValueError as e:
        print(e)

    except KeyboardInterrupt as e:
        print("Keyboard interrupt!")


if __name__ == "__main__":
    main()
