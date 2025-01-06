"""

Write a Python program to empty a variable without destroying it.

    Sample data: n=20
    d = {"x":200}
    Expected Output : 0
    {}

"""


def main():
    # Define a variable n with a value of 20.
    n = 20

    # Define a dictionary d with a key "x" and a value of 200.
    d = {"x": 200}

    # Define a list l with elements 1, 3, and 5.
    l = [1, 3, 5]

    # Define a tuple t with elements 5, 7, and 8.
    t = (5, 7, 8)

    # Print the type of n and create an instance of that type with no arguments.
    print(type(n)())

    # Print the type of d and create an instance of that type with no arguments.
    print(type(d)())

    # Print the type of l and create an instance of that type with no arguments.
    print(type(l)())

    # Print the type of t and create an instance of that type with no arguments.
    print(type(t)())


if __name__ == "__main__":
    main()
