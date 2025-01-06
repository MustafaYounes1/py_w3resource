"""

Write a Python program to get the current username.

"""

# access user-related functionality
import getpass


def main():
    print(f"Current user name: {getpass.getuser()}")


if __name__ == "__main__":
    main()
