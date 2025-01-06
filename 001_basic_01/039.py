"""
[Weird Exercise]

Write a Python program to compute the future value of a specified principal amount, rate of interest,
and number of years.

Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79

Hint: The formula for future value with compound interest is FV = P(1 + r/n)^nt.
FV = the future value;
P = the principal;
r = the annual interest rate expressed as a decimal;
n = the number of times interest is paid each year;
t = time in years.

"""


def main():
    # Define the principal amount (initial investment).
    amt = 10000
    # Define the annual interest rate as a percentage.
    int = 3.5
    # Define the number of years.
    years = 7
    # Calculate the future value of the investment using the compound interest formula.
    future_value = amt * ((1 + (0.01 * int)) ** years)
    # Round the future value to two decimal places and print it.
    print(round(future_value, 2))


if __name__ == "__main__":
    main()
