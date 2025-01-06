"""

Write a Python program to get the Identity, Type, and Value of an object.

"""


def main():
    x = 1

    # Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for
    # this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
    # CPython implementation detail: This is the address of the object in memory.
    print(f"Identity:   {id(x)}")
    print(f"Type:       {type(x)}")
    print(f"Value:      {x}")


if __name__ == "__main__":
    main()
