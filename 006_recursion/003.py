"""

Write a Python program to sum recursion lists using recursion.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21

"""


def sum_nested_with_recursion(lst):
    if not lst:
        return 0

    elif isinstance(lst[0], int):
        return lst[0] + sum_nested_with_recursion(lst[1:])

    elif isinstance(lst[0], list):
        return sum_nested_with_recursion(lst[0]) + sum_nested_with_recursion(lst[1:])

    else:
        raise ValueError("The list should contain only integers or lists of integers")


def main():
    lst = [1, 2, [3, 4], [5, 6]]
    print(sum_nested_with_recursion(lst))


if __name__ == "__main__":
    main()
