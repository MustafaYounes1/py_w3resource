"""

We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile but as few
as possible. Write a Python program to find the number of stones in each pile.

Input: 2    =>  [2, 4]
Input: 10   =>  [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3    =>  [3, 5, 7]
Input: 17   =>  [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

"""


def main():
    n = int(input("Enter a number: "))
    res = [n] + [n + _ * 2 for _ in range(n)]
    print(res)


if __name__ == "__main__":
    main()
