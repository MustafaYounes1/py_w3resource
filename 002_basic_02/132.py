"""

Write a Python program to find all the factors of a given natural number.
Factors:
The factors of a number are the numbers that divide into it exactly. The number 12 has six factors:
1, 2, 3, 4, 6 and 12 If 12 is divided by any of the six factors then the answer will be a whole number. For example:
12 / 3 = 4

Original Number: 1      =>  {1}
Original Number: 12     =>  {1, 2, 3, 4, 6, 12}
Original Number: 100    =>  {1, 2, 4, 100, 5, 10, 50, 20, 25}

"""


def find_divisors(n):
    divisors = {1, n}
    for _ in range(2, n // 2 + 1):
        if n % _ == 0:
            divisors.add(_)

    return divisors


def main():
    n = int(input("Enter a number: "))
    print(find_divisors(n))

if __name__ == "__main__":
    main()
