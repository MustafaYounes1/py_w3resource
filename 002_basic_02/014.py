"""

Write a Python program to add two positive integers without using the '+' operator.

Note: Use bit wise operations to add two numbers.
see https://iq.opengenus.org/addition-using-bitwise-operations/

"""


def bitwise_add(a, b):
    """
    A truth table will give a better understanding of how the binary addition takes place
            a   b   carry   sum
            0   0   0       0
            0   1   0       1
            1   0   0       1
            1   1   1       0
    From the truth table, we infer that:
        The carry expression is A & B
        The Sum expression is A ^ B
    """
    if b == 0:
        return a
    else:
        return bitwise_add(a ^ b, (a & b) << 1)


def main():
    x, y = [int(_) for _ in input("Enter two space-separated integers: ").split()]
    print(bitwise_add(x, y))


if __name__ == "__main__":
    main()
