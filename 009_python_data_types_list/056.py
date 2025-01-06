"""

Write a Python program to convert a string to a list.

color = "['Red', 'Green', 'White']"

['Red', 'Green', 'White']

"""

# Import the 'ast' (Abstract Syntax Trees) module, which provides a safe way to evaluate Python literals
import ast


def main():
    color = "['Red', 'Green', 'White']"

    # Use the 'ast.literal_eval' function to safely evaluate the string as a Python literal expression
    # This function ensures that the string is treated as a valid Python literal, in this case, a list
    print(ast.literal_eval(color))


if __name__ == "__main__":
    main()
