"""

Write a Python program to compute the amount of debt in n months. Each month, the loan adds 5% interest to the
$100,000 debt and rounds to the nearest 1,000 above.
Input:
An integer n (0 <= n <= 100)

Input number of months:     7
Amount of debt:             $144000

"""


def monthly_interest(d):
    interest = d * 1.05
    if interest % 1000:
        return (1 + interest // 1000) * 1000
    else:
        return interest


def debt(d, months):
    for _ in range(months):
        d = monthly_interest(d)

    return d


def main():
    d = float(input("Enter the debt: "))
    m = int(input("Enter the number of months: "))
    print(debt(d, m))


if __name__ == "__main__":
    main()
