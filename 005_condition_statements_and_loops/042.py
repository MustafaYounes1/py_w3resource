"""

Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

"""

from statistics import mean


def main():
    nums = []
    while True:
        n = int(input("Enter a number (0 to exit): "))

        if not n:
            break

        nums.append(n)

    print(f"Sum: {sum(nums)}, mean: {mean(nums)}")


if __name__ == "__main__":
    main()
