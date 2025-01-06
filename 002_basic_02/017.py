"""

Write a Python program to get all strobogrammatic numbers that are of length n.
A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears the same when rotated
180 degrees. In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).

For example,
Given n = 2, return "11", "69", "88", "96".
Given n = 3, return '818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689'
Given n = 3, return 8008 1001 9006 6009 8888 1881 9886 6889 8118 1111 9116 6119 8968 1961 9966 6969 8698 1691 9696 6699

When generating a strobogrammatic number, we are interested in filling in the first and last digits, which are paired.
The only pairs of digits that form valid strobogrammatic numbers are:

("1", "1")
("6", "9")
("9", "6")
("8", "8")
("0", "0") (but only in the middle of the number, because a number can't start with 0 unless it's "0" itself).

"""


def get_strobo(n):
    # Call the helper function with the given length 'n'.
    return strobo_helper(n, n)


def strobo_helper(n, length):
    # Base case: when 'n' is 0, return an empty string.
    if n == 0:
        return [""]

    # Base case: when 'n' is 1, return the strobogrammatic digits for length 1.
    if n == 1:
        return ["1", "0", "8"]

    # Recursive case: generate strobogrammatic numbers for 'n-2'.
    middles = strobo_helper(n-2, length)

    result = []

    # Iterate over the generated middles and create strobogrammatic numbers.
    for middle in middles:
        # If 'n' is not equal to the original length, add "0" on both sides.
        if n != length:
            result.append("0" + middle + "0")

        # Add strobogrammatic numbers with "8" in the middle.
        result.append("8" + middle + "8")

        # Add strobogrammatic numbers with "1" in the middle.
        result.append("1" + middle + "1")

        # Add strobogrammatic numbers with "9" in the first half and "6" in the second half.
        result.append("9" + middle + "6")

        # Add strobogrammatic numbers with "6" in the first half and "9" in the second half.
        result.append("6" + middle + "9")

    return result


def main():
    n = int(input("Enter an integer: "))

    for _ in get_strobo(n):
        print(_, end=" ")


if __name__ == "__main__":
    main()
