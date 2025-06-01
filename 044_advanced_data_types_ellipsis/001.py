"""

Write a Python function that takes an arbitrary number of arguments using *args and prints each argument.
Use ... to represent unspecified arguments.

func(1, "hello", 2.0)
->      Arg 0: 1
        Arg 1: hello
        Arg 2: 2.0

func()
->      Ellipsis

"""


def func(*args: ...) -> None:
    if not args:
        print(...)
    else:
        for i, arg in enumerate(args):
            print(f"Arg {i}: {arg}")


def main():
    func(1, "hello", 2.0)
    func()


if __name__ == "__main__":
    main()
