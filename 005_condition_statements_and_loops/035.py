"""

Write a Python program that checks whether a string represents an integer or not.
Expected Output:

Input a string: Python
The string is not an integer

"""


def main():
    s = input("Enter a string: ")
    print(f"The string {['is not', 'is'][s.isdigit()]} integer.")


if __name__ == "__main__":
    main()
