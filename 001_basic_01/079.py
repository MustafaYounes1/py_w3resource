"""

Write a Python program to get the size of an object in bytes.

Hint: use the 'sys' module

"""

import sys


def main():
    # Define three strings and assign values to them
    str1 = "one"
    str2 = "four"
    str3 = "three"
    x = 0
    y = 112
    z = 122.56

    # Print the size in bytes of each variable
    print("Size of ", str1, "=", str(sys.getsizeof(str1)) + " bytes")
    print("Size of ", str2, "=", str(sys.getsizeof(str2)) + " bytes")
    print("Size of ", str3, "=", str(sys.getsizeof(str3)) + " bytes")
    print("Size of", x, "=", str(sys.getsizeof(x)) + " bytes")
    print("Size of", y, "=", str(sys.getsizeof(y)) + " bytes")

    # Define a list and assign values to it
    L = [1, 2, 3, 'Red', 'Black']

    # Print the size in bytes of the list
    print("Size of", L, "=", sys.getsizeof(L), " bytes")

    # Define a tuple and assign values to it
    T = ("Red", [8, 4, 6], (1, 2, 3))

    # Print the size in bytes of the tuple
    print("Size of", T, "=", sys.getsizeof(T), " bytes")

    # Define a set and assign values to it
    S = {'apple', 'orange', 'apple', 'pear'}

    # Print the size in bytes of the set
    print("Size of", S, "=", sys.getsizeof(S), " bytes")

    # Define a dictionary and assign values to it
    D = {'Name': 'David', 'Age': 6, 'Class': 'First'}

    # Print the size in bytes of the dictionary
    print("Size of", D, "=", sys.getsizeof(S), " bytes")


if __name__ == "__main__":
    main()
