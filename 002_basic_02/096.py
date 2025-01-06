"""

Write a Python program to check whether a given number is a narcissistic number or not.

If you are a reader of Greek mythology, then you are probably familiar with Narcissus. He was a hunter of exceptional
beauty that he died because he was unable to leave a pool after falling in love with his own reflection. That's why I
keep myself away from pools these days (kidding).

In mathematics, he has kins by the name of narcissistic numbers - numbers that can't get enough of themselves.
In particular, they are numbers that are the sum of their digits when raised to the power of the number of digits.

For example, 371 is a narcissistic number; it has three digits, and if we cube each digits 33 + 73 + 13 the sum is 371.

Other 3-digit narcissistic numbers are
153 = 1^3 + 5^3 + 3^3
370 = 3^3 + 7^3 + 0^3
407 = 4^3 + 0^3 + 7^3.

There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
1634 = 1^4+6^4+3^4+4^4
8208 = 8^4+2^4+0^4+8^4
9474 = 9^4+4^4+7^4+4^4

It has been proven that there are only 88 narcissistic numbers (in the decimal system) and that the largest of which is
115,132,219,018,763,992,565,095,597,973,971,522,401; has 39 digits.

Sample Input:
(153)   =>  True
(370)   =>  True
(407)   =>  True
(409)   =>  False
(1634)  =>  True
(8208)  =>  True
(9474)  =>  True
(9475)  =>  False

"""


def is_narcissistic(n):
    return str(
        sum(
            [pow(int(_), len(n)) for _ in n]
        )
    ) == n


def main():
    s = input("Enter a number: ")
    print(is_narcissistic(s))


if __name__ == "__main__":
    main()
