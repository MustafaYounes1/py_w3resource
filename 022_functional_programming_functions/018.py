"""

Write a Python program to execute a string containing Python code.

def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))

>   Multiply of 2 and 3 is:  6

"""


def execute_from_str(s: str) -> None:
    exec(s)


def main():
    code = """
def multiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',multiply(2,3))
    """

    execute_from_str(code)


if __name__ == "__main__":
    main()
